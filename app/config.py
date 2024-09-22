import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
db = SQLAlchemy()

class Database:
    
    def __init__(self, app) -> None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")#"postgresql://postgres:1234@localhost:5432/TEST_1"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        db.init_app(app)