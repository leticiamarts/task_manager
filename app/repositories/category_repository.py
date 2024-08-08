from models.category import Category
from database import db

class CategoryRepository:
    @staticmethod
    def get_category_by_id(category_id):
        return Category.query.get(category_id)

    @staticmethod
    def create_category(name):
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return new_category
    
    @staticmethod
    def exists_by_name(name: str) -> bool:
        return Category.query.filter_by(name=name).first() is not None
