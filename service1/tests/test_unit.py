from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_open_list(self):
        response = self.client.get(url_for('list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hey', response.data)


    def test_spirit_on_page(self):
        with patch("requests.get") as g:
                with patch("requests.post") as p:
                    g.return_value.text = "Vodka"
                    p.return_value.text = "Orange Juice"

                    response = self.client.get(url_for("index"))
                    self.assertEqual(response.status_code, 200)
                    self.assertIn(b'Have a Vodka with Orange Juice', response.data)

        with patch("requests.get") as e:
                e.return_value.text = "0.33"
                response = self.client.get(url_for("index"))
                self.assertEqual(response.status_code, 200)