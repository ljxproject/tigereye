from flask_script import Manager, Server, Shell
from tigereye.app import create_app
from tigereye.configs.default import DefaultConfig
from tigereye.models import db
from tigereye.models.movie import Movie
from tigereye.models.cinema import Cinema
from tigereye.models.hall import Hall
from tigereye.models.order import Order
from tigereye.models.play import Play
from tigereye.models.seat import Seat, PlaySeat


app = create_app(config=DefaultConfig)
manager = Manager(app)
manager.add_command('run', Server('127.0.0.1', port=8000))


def _make_context():
    from tigereye.api.misc import MiscView
    locals().update(globals())
    return dict(**locals())

manager.add_command('shell', Shell(make_context=_make_context))


@app.route('/hello')
def hello():
    return 'hello world'


@manager.command
def createdb():
    db.create_all()


@manager.command
def testdata():
    Movie.create_test_data(100)
    Cinema.create_test_data(cinema_num=10)

if __name__ == '__main__':
    manager.run()