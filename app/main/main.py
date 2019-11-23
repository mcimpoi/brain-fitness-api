#!flask/bin/python
from flask import Flask, Blueprint
from model.Teacher import Teacher
from model.Admin import Admin
from model.User import User

app = Flask(__name__)

# for testin
userObject = {'userID': '-1', 'username': 'test'}

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/')
def index():
    return "Hello, World!"


@api_bp.route('/testUser')
def createTestNewUser():
    return 'Created Test New Users'


@api_bp.route('/createUser')
def createNewUser():
    output = User.createUser(userObject)
    return output


@app.route('/userCreateNewUser')
def userCreateNewUser(user_object):
    output = Admin.userCreateNewUser(userObject)
    return output


if __name__ == '__main__':
    app.run(debug=True)
