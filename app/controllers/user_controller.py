from flask import request, jsonify
from services.user_service import UserService
from dtos.user_dto import UserDTO

class UserController:
    @staticmethod
    def get_user(identifier_number):
        user = UserService.get_user(identifier_number)
        if user:
            user_dto = UserDTO(user.identifier_number, user.username, user.email)
            return jsonify(user_dto.__dict__)
        return jsonify({'error': 'User not found'}), 404

    @staticmethod
    def create_user():
        data = request.json
        username = data.get('username')
        email = data.get('email')
        identifier_number = data.get('identifier_number')
        user = UserService.create_user(username, email, identifier_number)
        user_dto = UserDTO(user.identifier_number, user.username, user.email)
        return jsonify(user_dto.__dict__), 201
