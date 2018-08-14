import functools
from flask import request
from flask.json import jsonify

from tigereye.helpers.code import Code


class Validator(object):

    def __init__(self, **params_template):
        self.pt = params_template

    def __call__(self, func):
        @functools.wraps(func)
        def decorated_function(*args, **kwargs):
            try:
                request.params = {}
                for p, f in self.pt.items():
                    request.params[p] = f(request.values[p])
            except Exception:
                response = jsonify(
                    rc=Code.required_parameter_missing.value,
                    msg=Code.required_parameter_missing.name,
                    data={'required_params': p}
                )
                response.status_code = 400
                return response
            return func(*args, **kwargs)
        return decorated_function


def multi_int(values, sperator=',', can_be_empty=False):
    if can_be_empty and not values:
        return []
    return [int(i) for i in values.split(sperator)]
