from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestVolume(TestBase):
    def test_spirit(self):
        volume = [b'0.33', b'0.5', b'0.7']
        response = self.client.get(url_for('volume'))
        self.assertIn(response.data, volume)