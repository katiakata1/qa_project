from unittest.mock import patch
from flask import Flask, url_for, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_vodka(self):
        with patch("requests.post") as v:
            v.return_value.text == "Vodka"
            with patch("random.choices") as r:
                r.return_value.text = "Orange Juice"
                response = self.client.post(
                url_for('mixer'),
                data = 'Vodka')
                self.assertEqual(response.status_code, 200)

    def test_gin(self):
        with patch("requests.post") as gin:
            gin.return_value.text == "Gin"
            with patch("random.choices") as r:
                r.return_value.text = "Tonic"
                response = self.client.post(
                url_for('mixer'),
                data = 'Gin')
                self.assertEqual(response.status_code, 200)
    
    def test_rum(self):
        with patch("requests.post") as rum:
            rum.return_value.text == "Rum"
            with patch("random.choices") as r:
                r.return_value.text = "Coke"
                response = self.client.post(
                url_for('mixer'),
                data = 'Rum')
                self.assertEqual(response.status_code, 200)

    def test_Jagermeister(self):
        with patch("requests.post") as Jagermeister:
            Jagermeister.return_value.text == "Jagermeister"
            with patch("random.choices") as r:
                r.return_value.text = "Red Bull"
                response = self.client.post(
                url_for('mixer'),
                data = 'Jagermeister')
                self.assertEqual(response.status_code, 200)