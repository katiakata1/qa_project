from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestSpirit(TestBase):
    def test_spirit(self):
        spirit = [b'Vodka', b'Gin', b'Rum', b'Jagermeister']
        response = self.client.get(url_for('spirit'))
        self.assertIn(response.data, spirit)

