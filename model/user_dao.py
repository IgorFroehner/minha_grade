
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from app import db


class User(db.Document):
    user = db.StringField()
    password = db.StringField()
    authenticated = False
    schedule = db.ReferenceField('Schedule')

    def get_id(self):
        return self.user

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


class LoginForm(FlaskForm):
    user = StringField()
    password = PasswordField()


def find_by_user(user: str) -> User:
    return User.objects(user=user).first()
