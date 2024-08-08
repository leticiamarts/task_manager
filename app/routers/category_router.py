from flask import Blueprint
from controllers.category_controller import CategoryController

category_router = Blueprint('category', __name__)

@category_router.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    return CategoryController.get_category(category_id)

@category_router.route('/categories', methods=['POST'])
def create_category():
    return CategoryController.create_category()
