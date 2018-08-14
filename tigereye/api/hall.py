from flask import request
from tigereye.api import ApiView
from tigereye.helpers.code import Code
from tigereye.models.hall import Hall
from tigereye.models.seat import Seat, SeatType


class HallView(ApiView):

    def seats(self):
        hid = request.args['hid']
        hall = Hall.get(hid)
        if not hall:
            return Code.hall_does_not_exist
        hall.seats = Seat.query.filter(
            Seat.hid == hid,
            Seat.seat_type != SeatType.road.value
        ).all()
        return hall