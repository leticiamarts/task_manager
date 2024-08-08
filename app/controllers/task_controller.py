from flask import request, jsonify
from services import task_service
from services.task_service import TaskService
from dtos.task_dto import TaskDTO

class TaskController:
    @staticmethod
    def get_task(task_id):
        task = TaskService.get_task(task_id)
        if task:
            task_dto = TaskDTO(task.id, task.title, task.description, task.category_id)
            return jsonify(task_dto.__dict__)
        return jsonify({'error': 'Task not found'}), 404

    @staticmethod
    def create_task():
        data = request.get_json()
        task_dto = TaskDTO(title=data['title'], description=data['description'], category_id=data['category_id'])
        
        try:
            task = task_service.create_task(task_dto)
            return jsonify(task.to_dict()), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
