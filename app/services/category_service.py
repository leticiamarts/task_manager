from dtos.category_dto import CategoryDTO
from models.category import Category
from repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    @staticmethod
    def get_category(category_id):
        return CategoryRepository.get_category_by_id(category_id)

    @staticmethod
    def create_category(category_dto: CategoryDTO) -> Category:
        category_repository = CategoryRepository()
        if category_repository.exists_by_name(category_dto.name):
            raise ValueError(f"Category with name '{category_dto.name}' already exists.")
        
        category = Category(name=category_dto.name)
        return category_repository.create_category(category.name)