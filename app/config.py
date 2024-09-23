import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class Database:
    
    def __init__(self, app) -> None:
        load_dotenv()
        print("RC1 ", os.getenv("DATABASE_URL"))
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mateo:Sanmiguel99+@pptgame.postgres.database.azure.com:5432/test"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        print("RCV ",app.config['SQLALCHEMY_DATABASE_URI'])
        
        db.init_app(app)
        print(app)