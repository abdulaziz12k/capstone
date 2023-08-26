import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# DB CONNECTION VARIABLES TO RENDER POSTGERSQL DATABASE
# DB_HOST = os.getenv('DB_HOST', 'dpg-cisgogh5rnujejoug2e0-a')
# DB_USER = os.getenv('DB_USER', 'student')
# DB_PASSWORD = os.getenv('DB_PASSWORD', 'TT6DpQOzAiQa4wlx0aZOBPr9nNdTFimB')
# DB_NAME = os.getenv('DB_NAME', 'capstone_l9pt')
# database_path = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'student')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'student')
DB_NAME = os.getenv('DB_NAME', 'capstone')
database_path = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    with app.app_context():
        db.create_all()
