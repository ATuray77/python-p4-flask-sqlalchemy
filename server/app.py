#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db


app = Flask(__name__)  # flask application instance creation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' # this represents the database URL to connect with(app.db)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

migrate = Migrate(app, db)  # migration instance creation

db.init_app(app)  # initializes our application(app) for use within  our database configuration with 

if __name__ == '__main__':  # script
    app.run(port=5555, debug=True)
