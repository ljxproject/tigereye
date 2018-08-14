from tigereye.api import ApiView
from flask_classy import route

from tigereye.helpers.validator import Validator


class MiscView(ApiView):

    def before_check(self):
        print('hahahaah')

    def check(self):
        return "I'm OK"

    def ping(self):
        return 'pong'

    def error(self):
        num = 0
        1 / num