from repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_user(identifier_number):
        return UserRepository.get_user_by_identifier(identifier_number)

    @staticmethod
    def create_user(username, email, identifier_number):
        if UserRepository.exists_by_identifier_number(identifier_number):
            raise ValueError(f"User with identifier number '{identifier_number}' already exists.")
        return UserRepository.create_user(username, email, identifier_number)
