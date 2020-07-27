from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer

database_name = "app_db"
database_path = "postgres://admin:secret@{}/{}".format('192.168.99.100:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    Migrate(app, db)


def commit_session():
    db.session.commit()

# TODO MODELS Account & Transaction 