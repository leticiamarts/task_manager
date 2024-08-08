from flask import Blueprint
from controllers.user_controller import UserController

user_router = Blueprint('user', __name__)

@user_router.route('/users/<identifier_number>', methods=['GET'])
def get_user(identifier_number):
    return UserController.get_user(identifier_number)

@user_router.route('/users', methods=['POST'])
def create_user():
    return UserController.create_user()
