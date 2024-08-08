from models.task import Task
from dtos.task_dto import TaskDTO
from repositories.task_repository import TaskRepository

class TaskService:

    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository


    @staticmethod
    def get_task(task_id):
        return TaskRepository.get_task_by_id(task_id)

    @staticmethod
    def create_task(self, task_dto: TaskDTO) -> Task:
        if self.task_repository.exists_by_title(task_dto.title):
            raise ValueError(f"Task with title '{task_dto.title}' already exists.")
        
        task = Task(title=task_dto.title, description=task_dto.description, category_id=task_dto.category_id)
        return self.task_repository.save(task)
