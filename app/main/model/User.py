from .. import db

USERNAME_LENGTH = 128
EMAIL_LENGTH = 128
PASSWORD_HASH_LENGTH = 256


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(USERNAME_LENGTH), unique=True, nullable=False)
    email = db.Column(db.String(EMAIL_LENGTH), unique=True, nullable=False)
    usertype = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Integer, nullable=False)  # put 0 or 1
    password = db.Column(db.String(PASSWORD_HASH_LENGTH))
    # TODO: support picture