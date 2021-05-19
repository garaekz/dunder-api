# -*- coding: utf-8 -*-
__version__ = '0.0.1'

import os
from dotenv import load_dotenv
from flask import Flask, json
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
load_dotenv() 

server = Flask(__name__)
server.debug = os.getenv("DEBUG")
server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DSN", "sqlite:///test.db")
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(server)
db.create_all()
migrate = Migrate(server, db)
ma = Marshmallow(server)

@server.errorhandler(HTTPException)
def handle_exception(e):
    """Retorna JSON en lugar de HTML en caso de errores HTTP."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

from app.controllers import *