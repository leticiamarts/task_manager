# Task Manager API
 This is a simple task manager API built with Flask, which allows users to create, retrieve, and manage tasks and categories. The project is structured with a clear separation of concerns, including models, DTOs, controllers, services, and repositories.

## Installation

### Clone the repository
```
git clone https://github.com/yourusername/task_manager.git
cd task_manager
```

### Setup Environment
It's recommended to use a virtual environment to manage dependencies.
```
python -m venv .venv
```
- On Windows:
```
.venv\Scripts\activate
```
- On Linux/MacOS:
```
source .venv/bin/activate
```

With the environment setup, on root, install the dependencies:
```
pip install -r requirements.txt
```

Set Variables inside .env file that you will create on root:
```
DATABASE_URL=mysql+pymysql://your_username:your_password@your_localhost:port/db_name
```
Don't forget to change `your_username`, `your_password`, `your_localhost`, `port` and `db_name` for it's personal content.

## Running Application
On shell, run:
```
python app/main.py
```
The API will be available on the link at your shell.


## API routs

The API follows RESTful principles and includes the following endpoints:

- Users
    - GET /api/users/{identifier_number}: Retrieve a user by their identifier number.
    - POST /api/users: Create a new user.


- Tasks
    - GET /api/tasks/{task_id}: Retrieve a task by its ID.
    - POST /api/tasks: Create a new task.


- Categories
    - GET /api/categories/{category_id}: Retrieve a category by its ID.
    - POST /api/categories: Create a new category.

### Example request
To create a new task, send a POST request to /api/tasks with a JSON body:
```
{
  "title": "Task Title",
  "description": "Task Description",
  "category_id": 1
}
```
