# -*- coding: utf-8 -*-
from app import db, server
from app.models.Personaje import Personaje, PersonajeSchema
from flask import jsonify
from healthcheck import EnvironmentDump

envdump = EnvironmentDump(include_python=False,
                          include_os=False,
                          include_process=False)

''' @server.route("/")
def index():
    return "Hola Puerk!"
 '''
def info():
  return {"maintainer": "David Garay", 
    "git_repo": "https://github.com/garaekz/dunder-api"}
    
envdump.add_section("app", info)
server.add_url_rule("/", "environment", view_func=lambda: envdump.run())

@server.route("/test")
def index():
    personajes = Personaje.query.all()
    personajes_schema = PersonajeSchema(many=True)
    return jsonify(personajes_schema.dump(personajes))

@server.route("/create")
def create():
    personaje = Personaje(nombre="Michael Scott")
    personaje_schema = PersonajeSchema()
    db.session.add(personaje)
    db.session.commit()
    return personaje_schema.dump(personaje)