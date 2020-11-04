import dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase

from blog import env

dotenv.load_dotenv()

app = Flask(__name__)
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = env.SQLALCHEMY_UNITTEST_DATABASE_URI
app.config["SQLALCHEMY_ECHO"] = env.SQLALCHEMY_ECHO
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app=app)


class BaseTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.drop_all()

    def create_app(self):
        return app
