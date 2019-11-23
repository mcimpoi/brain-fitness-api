from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash

# import pdb

from .model.User import User
from . import db

auth = Blueprint('auth', __name__)

USER_TYPE_TEACHER = 1
USER_TYPE_ADMIN = 1729


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, username=username,
                    password=generate_password_hash(password + username, method='sha256'),
                    usertype=USER_TYPE_TEACHER,
                    active=1)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return 'Logout'