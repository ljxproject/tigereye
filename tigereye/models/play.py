from sqlalchemy import text
from sqlalchemy.sql import func
from tigereye.models import db, Model


"""
    ID
    电影ID
    影院ID
    影厅ID
    价格类型
    原价
    售价
    最低价
    开始时间
    时长
    创建时间
    最后更新时间
    状态
"""


class Play(db.Model, Model):
    pid = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer)
    hid = db.Column(db.Integer)
    mid = db.Column(db.Integer)

    start_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, default=0, nullable=False)

    price_type = db.Column(db.Integer)
    price = db.Column(db.Integer)
    market_price = db.Column(db.Integer)
    lowest_price = db.Column(db.Integer)

    created_time = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_time = db.Column(db.DateTime, onupdate=func.now())
    status = db.Column(db.Integer, default=0, nullable=False, index=True)
