from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режисcёры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Быков'),
})

movie: Model = api.model('Фильмы', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Омерзительная восьмерка'),
    'description': fields.String(required=True, max_length=250, example='фильм '),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=x6aFkwiOJwk'),
    'year': fields.Integer(required=True, max_length=100),
    'rating': fields.Float(required=True, max_length=7.8),
    'genre': fields.Nested(genre),
    'director':fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='log@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='123321'),
    'name': fields.String(required=True, max_length=100, example='Vasya'),
    'surname': fields.Integer(required=True, max_length=100, example='Vasichnik'),
    'genre': fields.Nested(genre)
})


