from flask import Flask

def create_app():
    app = Flask(__name__)

    from .todos.routes import todos_bp
    app.register_blueprint(todos_bp, url_prefix='/todos')

    return app
