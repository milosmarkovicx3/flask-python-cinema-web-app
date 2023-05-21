from flask_testing import TestCase
from flask_app import app
from main.service.impl.actor_impl import ActorImpl

class ActorTest(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        self.ai = ActorImpl()

    def test_find(self):
        with app.test_client() as client:
            response = client.get('/actor/', query_string={'value': '1'})
            assert response

    def test_find_all(self):
        with app.test_client() as client:
            response = client.get('/actor/s', query_string={'max': '5'})
            assert response