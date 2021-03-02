from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestVolume(TestBase):
    def test_spirit(self):
        volume = [b'1/3 ', b'1/2 ', b'7/10 ']
        response = self.client.get(url_for('volume'))
        self.assertIn(response.data, volume)