import time
import functools
from flask import request, Response, make_response, jsonify, current_app
from flask_classy import FlaskView
from tigereye.helpers.code import Code


class ApiView(FlaskView):

    def before_request(self, name, **args):
        self.request_start_time = time.time()

    def after_request(self, name, response):
        current_app.logger.info('%s response time: %s' %
                            (request.path, time.time() - self.request_start_time)
                            )
        return response

    @classmethod
    def make_proxy_method(cls, name):
        """Creates a proxy function that can be used by Flasks routing. The
        proxy instantiates the FlaskView subclass and calls the appropriate
        method.

        :param name: the name of the method to create a proxy for
        """

        i = cls()
        view = getattr(i, name)

        if cls.decorators:
            for decorator in cls.decorators:
                view = decorator(view)

        @functools.wraps(view)
        def proxy(**forgettable_view_args):
            # Always use the global request object's view_args, because they
            # can be modified by intervening function before an endpoint or
            # wrapper gets called. This matches Flask's behavior.
            del forgettable_view_args

            if hasattr(i, "before_request"):
                response = i.before_request(name, **request.view_args)
                if response is not None:
                    return response

            before_view_name = "before_" + name
            if hasattr(i, before_view_name):
                before_view = getattr(i, before_view_name)
                response = before_view(**request.view_args)
                if response is not None:
                    return response

            response = view(**request.view_args)
            if not isinstance(response, Response):
                response_type = type(response)
                if response_type == Code:
                    response = jsonify(
                        rc=response.value,
                        msg=response.name,
                        data=request.args
                    )
                elif response_type is not str:
                    response = jsonify(rc=0, msg='succ', data=response)

                response = make_response(response)

            after_view_name = "after_" + name
            if hasattr(i, after_view_name):
                after_view = getattr(i, after_view_name)
                response = after_view(response)

            if hasattr(i, "after_request"):
                response = i.after_request(name, response)

            return response

        return proxy