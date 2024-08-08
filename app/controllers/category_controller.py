from flask import request, jsonify
from services import category_service
from services.category_service import CategoryService
from dtos.category_dto import CategoryDTO

class CategoryController:
    @staticmethod
    def get_category(category_id):
        category = CategoryService.get_category(category_id)
        if category:
            category_dto = CategoryDTO(category.id, category.name)
            return jsonify(category_dto.__dict__)
        return jsonify({'error': 'Category not found'}), 404

    @staticmethod
    def create_category():
        data = request.get_json()
        category_dto = CategoryDTO(name=data['name'])
        
        try:
            category = CategoryService.create_category(category_dto)
            return jsonify(category.to_dict()), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
