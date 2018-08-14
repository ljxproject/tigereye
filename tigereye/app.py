from flask import Flask
from flask_classy import FlaskView

from tigereye.models import db, JSONEncoder


def create_app(config=None):
    app = Flask('tigereye')
    app.config.from_object(config)
    app.json_encoder = JSONEncoder
    configure_views(app)
    db.init_app(app)
    return app


def configure_views(app):
    from tigereye.api.misc import MiscView
    from tigereye.api.movie import MovieView
    from tigereye.api.cinema import CinemaView
    from tigereye.api.hall import HallView
    from tigereye.api.play import PlayView
    from tigereye.api.seat import SeatView
    for view in locals().values():
        if type(view) == type and issubclass(view, FlaskView):
            view.register(app)

# @app.route('/hello')
# def hello():
#     return 'hello world'
#
#
# if __name__ == '__main__':
#     app.run()