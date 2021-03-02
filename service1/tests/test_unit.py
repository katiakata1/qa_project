from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app, db, Lists

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='IT_IS_A_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        # Creating a test list
        sample1 = Lists(
            spirit = "Vodka",
            volume = "1/3 ",
            mixer = "Orange Juice",
        )

        # Save list to db
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


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
                    self.assertIn(b'Have a <b>Vodka</b> with <b>Orange Juice</b>', response.data)

    def test_volume_on_page(self):
        with patch("requests.get") as e:
                e.return_value.text = "1/3 "
                response = self.client.get(url_for("list"))
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'1/3 l of <b>Vodka</b> with <b>Orange Juice</b>', response.data)
