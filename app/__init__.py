from flask import Flask
from .config import Database

def create_app():
    app = Flask(__name__)
    Database(app)
    
    from .routes import register_routes
    register_routes(app)

    return app
