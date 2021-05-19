# -*- coding: utf-8 -*-
from app.models.Actor import Actor, ActorSchema
from app import db, server
from app.models.Personaje import Personaje, PersonajeSchema
from flask import jsonify, request
from marshmallow import ValidationError

@server.route("/api/v1/personaje/", defaults={'personaje_id': None}, methods = ['GET', 'POST', 'DELETE'])
@server.route('/api/v1/personaje/<string:personaje_id>', methods = ['GET', 'POST', 'DELETE'])
def personaje(personaje_id):
    personaje_schema = PersonajeSchema()
    personajes_schema = PersonajeSchema(many=True)
    """ Se hace una matriz para definir las funciones de CRUD """
    if request.method == 'GET' and not personaje_id:
      personajes = Personaje.query.all()
      personajes_schema = PersonajeSchema(many=True)
      return {"result": personajes_schema.dump(personajes)}

    elif request.method == 'GET':
      personaje = Personaje.query.filter_by(id=personaje_id).first()
      if personaje is None:
        return {"message": "No se encontró un personaje con el ID proporcionado", "code": 404}, 404

      return {"result": personaje_schema.dump(personaje), "code": 200}

    elif request.method == 'POST':
      json_data = request.get_json()
      # Validar si viene info en el data
      if not json_data:
        return {"message": "No se proporcionaron datos", "code": 400}, 400
      
      # Inicializamos un actor None para futuras validaciones
      actor_id = None

      if 'actor_id' in json_data:
        actor_id = json_data.pop('actor_id')
        actor = Actor.query.filter_by(id=actor_id).first()
        if actor is None:
          return {"message": "No existe un actor con el ID proporcionado en 'actor_id'", "code": 400}

      elif 'actor' in json_data:
        # Hay que abstraer lo siguiente para reutilizar lo del modelo Actor
        actor_schema = ActorSchema()
        actor_json_data = json_data.pop('actor')
        
        # Valida si cumple con el modelo actor
        try:
          actor_data = actor_schema.load(actor_json_data)
        except ValidationError as err:
          return {"message": "Error en validación del actor asociado al personaje", "errors": err.messages}, 422

        actor = Actor.query.filter_by(nombre=actor_json_data['nombre']).first()
        if actor is None:
          # Crea nuevo actor
          actor = Actor(**actor_data)
          db.session.add(actor)
        else:
          return {"message": "Ya existe un actor con ese nombre", "code": 400, "actor": actor_schema.dump(actor)}, 400
      else:
        return {"message": "No se proporcionó un actor vinculado a este personaje", "code": 400}, 400

      # Valida si cumple con el modelo
      try:
        data = personaje_schema.load(json_data)
      except ValidationError as err:
        return err.messages, 422

      personaje = Personaje.query.filter_by(nombre=data['nombre']).first()
      if personaje is None:
        # Crea nuevo personaje
        personaje = Personaje(actor=actor, **data)
        db.session.add(personaje)
        db.session.commit()
        return {"result": personaje_schema.dump(personaje), "code": 200}

      db.session.rollback()
      return {"message": "Ya existe un personaje con ese nombre", "code": 400, "personaje": personaje_schema.dump(personaje)}, 400
    
    # Faltan PUT/PATCH y DELETE
    elif request.method == 'DELETE':
      return "DELETE"

    # Tal vez retornar error 500/404
    else:
      return "NADA!!!"
