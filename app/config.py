import os
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Database:
    
    def __init__(self, app) -> None:
        load_dotenv(find_dotenv())
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("CONNT_STRING")#"postgresql://mateo:Sanmiguel99+@pptgame.postgres.database.azure.com:5432/test"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)