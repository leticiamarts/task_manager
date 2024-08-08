from flask import Blueprint
from controllers.task_controller import TaskController

task_router = Blueprint('task', __name__)

@task_router.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return TaskController.get_task(task_id)

@task_router.route('/tasks', methods=['POST'])
def create_task():
    return TaskController.create_task()
