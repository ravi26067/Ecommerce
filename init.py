from flask import Flask
from config import Config
from constants import *
import pymysql

from models import db


# def create_app():
#     config = Config('config.json')
#
#     app = Flask(__name__)
#     app.secret_key = config.get_app_config()[APP_SECRET_KEY]
#
#     app.config[MYSQL_CONFIG] = config.get_mysql_config()
#
#     return app

def create_app():
    config = Config('config.json')

    app = Flask(__name__)
    app.secret_key = config.get_app_config()[APP_SECRET_KEY]

    # MySQL connection URI for SQLAlchemy
    mysql_config = config.get_mysql_config()
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{mysql_config[MYSQL_USER]}:{mysql_config[MYSQL_PASSWORD]}"
        f"@{mysql_config[MYSQL_HOST]}/{mysql_config[MYSQL_DATABASE]}"
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app


def get_mysql_connection(app):
    mysql_config = app.config[MYSQL_CONFIG]
    return pymysql.connect(
        host=mysql_config[MYSQL_HOST],
        user=mysql_config[MYSQL_USER],
        password=mysql_config[MYSQL_PASSWORD],
        database=mysql_config[MYSQL_DATABASE]
    )
