from datetime import datetime

from sqlalchemy import inspect
from flask import json as _json
from flask_sqlalchemy import SQLAlchemy
from tigereye.helpers.tetime import SIMPLE_DATETIME_FORMAT

db = SQLAlchemy()

__all__ = ['hall', 'movie', 'cinema']


class Model(object):
    @classmethod
    def get(cls, primary_key):
        return cls.query.get(primary_key)

    @property
    def persistent(self):
        return inspect(self).persistent

    def put(self):
        db.session.add(self)

    @staticmethod
    def commit():
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()

    def save(self):
        try:
            self.put()
            self.commit()
        except Exception:
            self.rollback()

    def delete(self):
        db.session.delete(self)
        # self.commit()

    def __json__(self):
        _d = {}
        for k, v in vars(self).items():
            if not k.startswith('_'):
                _d[k] = v
        return _d


class JSONEncoder(_json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Model):
            return o.__json__()
        if isinstance(o, datetime):
            return o.strftime(SIMPLE_DATETIME_FORMAT)
        return _json.JSONEncoder.default(self, o)













