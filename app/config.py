from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Database:
    
    def __init__(self, app) -> None:
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mateo:Sanmiguel99+@pptgame.postgres.database.azure.com:5432/test"#"postgresql://postgres:1234@localhost:5432/TEST_1"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        db.init_app(app)