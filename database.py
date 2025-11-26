from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def init_db(app: Flask):
    # Railway MySQL connection
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://root:cSpXneUycqnISaIiJmhUbYzcpPgjUVOR@interchange.proxy.rlwy.net:18561/railway'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
