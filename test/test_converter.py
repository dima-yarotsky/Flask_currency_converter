import unittest
from flask_testing import TestCase
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Currency Converter', response.data)


    def test_convert_valid_input(self):
        data = {'from_currency': 'USD', 'to_currency': 'EUR', 'amount': '100'}
        response = self.app.post('/convert', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Currency Converter - Result</h1>', response.data)


if __name__ == '__main__':
    unittest.main()
