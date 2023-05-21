from flask_testing import TestCase
from flask_app import app
from main.service.impl.user_impl import UserImpl

class UserTest(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        self.ui = UserImpl()

    def test_find(self):
        with app.test_client() as client:
            response = client.get('/user/', query_string={'value': '1'})
            assert response

    def test_find_all(self):
        with app.test_client() as client:
            response = client.get('/user/s', query_string={'max': '5'})
            assert response

