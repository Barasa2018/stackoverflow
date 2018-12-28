import flask
from flask import request,json
import unittest
from app import app


class TestApi(unittest.TestCase):

    def test_add_user(self):
        response = self.app.post('/app/api/v1/users',
                                data=json.dumps(dict(name="Barasa",email="barasa@gmail.com")),
                                content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_fetch_user(self):
        response = self.app.get('/app/api/v1/users')
        response.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()