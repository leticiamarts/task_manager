from models.user import User

from database import db

class UserRepository:
    @staticmethod
    def get_user_by_identifier(identifier_number):
        return User.query.get(identifier_number)

    @staticmethod
    def create_user(username, email, identifier_number):
        new_user = User(username=username, email=email, identifier_number=identifier_number)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def exists_by_identifier_number(identifier_number):
        return User.query.filter_by(identifier_number=identifier_number).first() is not None
