from flask import request
from tigereye.api import ApiView
from tigereye.helpers.code import Code
from tigereye.models.hall import Hall
from tigereye.models.seat import Seat, SeatType, PlaySeat
from tigereye.helpers.validator import Validator


class PlayView(ApiView):

    @Validator(pid=int)
    def seats(self):
        pid = request.params['pid']
        return PlaySeat.query.filter(
            PlaySeat.pid == pid,
            PlaySeat.seat_type != SeatType.road.value
        ).all()
