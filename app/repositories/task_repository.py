from models.task import Task

from database import db

class TaskRepository:
    @staticmethod
    def get_task_by_id(task_id):
        return Task.query.get(task_id)

    @staticmethod
    def create_task(title, description, category_id):
        new_task = Task(title=title, description=description, category_id=category_id)
        db.session.add(new_task)
        db.session.commit()
        return new_task
    
    def exists_by_title(self, title: str) -> bool:
        return self.db_session.query(Task).filter_by(title=title).first() is not None
