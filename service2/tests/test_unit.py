from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimals(TestBase):
    def test_animal(self):
        animals = [b'Lion', b'Dog', b'Cat', b'Cow']
        response = self.client.get(url_for('animal'))
        self.assertIn(response.data, animals)

    def test_noise_lion(self):
        response = self.client.post(
            url_for('noise'),
            data="Lion",
            follow_redirects=True
        )
        self.assertIn(b'Roar', response.data)

    def test_noise_Dog(self):
        response = self.client.post(
            url_for('noise'),
            data="Dog",
            follow_redirects=True
        )
        self.assertIn(b'Woof', response.data)

    def test_noise_Cat(self):
        response = self.client.post(
            url_for('noise'),
            data="Cat",
            follow_redirects=True
        )
        self.assertIn(b'Meow', response.data)

    def test_noise_Cow(self):
        response = self.client.post(
            url_for('noise'),
            data="Cow",
            follow_redirects=True
        )
        self.assertIn(b'Mooo', response.data)



