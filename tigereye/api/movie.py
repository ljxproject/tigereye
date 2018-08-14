from flask import request
from tigereye.models.movie import Movie
from tigereye.api import ApiView
from tigereye.helpers.code import Code


class MovieView(ApiView):

    def all(self):
        return Movie.query.all()

    def get(self):
        mid = request.args['mid']
        movie = Movie.get(mid)
        if not movie:
            return Code.movie_does_not_exist
        return movie
