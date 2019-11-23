import json

from .. import db

USERNAME_LENGTH = 128
EMAIL_LENGTH = 128
PASSWORD_HASH_LENGTH = 256

USER_TYPE_TEACHER = 1
USER_TYPE_ADMIN = 1729


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(USERNAME_LENGTH), unique=True, nullable=False)
    email = db.Column(db.String(EMAIL_LENGTH), unique=True, nullable=False)
    usertype = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Integer, nullable=False)  # put 0 or 1
    password = db.Column(db.String(PASSWORD_HASH_LENGTH))
    # TODO: support picture

    @staticmethod
    def createUser(user_details: dict) -> str:
        """Receives dict (json?) with details of user to create
        minimum: username, email, password
        @return string with status (?)
        """
        username = user_details.get('username', None)
        if username is None:
            return 'No username provided'
        email = user_details.get('email', None)
        if email is None:
            return 'No email was provided'

        # should be only one
        user_by_name = User.query.filter_by(username=username).first()
        if user_by_name is not None:
            return 'User already exists'

        user_by_email = User.query.filter_by(username=email).first()
        if user_by_email is not None:
            return 'Email already registered'

        new_user = User(email=email, username=username, password=user_details['password'],
                        usertype=USER_TYPE_TEACHER, active=1)

        db.session.add(new_user)
        db.session.commit()

        return 'Created user'
