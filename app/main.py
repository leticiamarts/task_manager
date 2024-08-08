from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from database import db
from models.user import User
from models.task import Task
from models.category import Category
from routers.user_router import user_router
from routers.task_router import task_router
from routers.category_router import category_router


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:3308/tasks_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db.init_app(app)

# Registra os blueprints
app.register_blueprint(user_router, url_prefix='/api')
app.register_blueprint(task_router, url_prefix='/api')
app.register_blueprint(category_router, url_prefix='/api')

# Configuração do Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Gerenciador de Tarefas API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Servir o arquivo swagger.json
@app.route('/static/swagger.json')
def swagger_spec():
    return send_from_directory('.', 'swagger.json')

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True)