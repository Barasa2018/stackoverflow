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
        self.assertEqual(response.status_code,200)

    def test_add_question(self):
        response = self.app.post('/app/api/v1/questions',
                                data=json.dumps(dict(title='CSS',description='I need help with inline CSS')),
                                content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_fetch_questions(self):
        response = self.app.get('/app/api/v1/questions')
        self.assertEqual(response.status_code,200)

    def test_fetch_question(self):
        response = self.app.get('/app/api/v1/questions/<int:id>')
        self.assertEqual(response.status_code,200)

    def test_user_questions(self):
        response = self.app.get('/app/api/v1/users/<int:id>/questions')
        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()