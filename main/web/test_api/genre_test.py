from flask_testing import TestCase
from flask_app import app
from main.service.impl.genre_impl import GenreImpl


class GenreTest(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        self.gi = GenreImpl()

    def test_find(self):
        with app.test_client() as client:
            response = client.get('/genre/', query_string={'value': '1'})
            assert response

    def test_find_all(self):
        with app.test_client() as client:
            response = client.get('/genre/s', query_string={'max': '5'})
            assert response