import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy




class Database:
    
    def __init__(self, app) -> None:
        load_dotenv()
        print("RC1 ", os.getenv("DATABASE_URL"))
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mateo:Sanmiguel99+@pptgame.postgres.database.azure.com:5432/test"#"postgresql://postgres:1234@localhost:5432/TEST_1"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        print("RCV ",app.config['SQLALCHEMY_DATABASE_URI'])
        
        db = SQLAlchemy(app)
        db.init_app(app)