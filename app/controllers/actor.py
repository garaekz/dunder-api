# -*- coding: utf-8 -*-
from app import db, server
from app.models.Actor import Actor, ActorSchema
from flask import jsonify, request
from marshmallow import ValidationError

@server.route("/api/v1/actor/", defaults={'actor_id': None}, methods = ['GET', 'POST', 'DELETE'])
@server.route('/api/v1/actor/<string:actor_id>', methods = ['GET', 'POST', 'DELETE'])
def actor(actor_id):
    actor_schema = ActorSchema()
    actors_schema = ActorSchema(many=True)
    """ Se hace una matriz para definir las funciones de CRUD """
    if request.method == 'GET' and not actor_id:
      actors = Actor.query.all()
      actors_schema = ActorSchema(many=True)
      return {"result": actors_schema.dump(actors)}

    elif request.method == 'GET':
      actor = Actor.query.filter_by(id=actor_id).first()
      if actor is None:
        return {"message": "No se encontró un actor con el ID proporcionado", "code": 404}, 404

      return {"result": actor_schema.dump(actor), "code": 200}

    elif request.method == 'POST':
      json_data = request.get_json()
      # Validar si viene info en el data
      if not json_data:
        return {"message": "No se proporcionaron datos", "code": 400}, 400

      # Valida si cumple con el modelo
      try:
        data = actor_schema.load(json_data)
      except ValidationError as err:
        return {"message": "Error en validación", "errors": err.messages}, 422

      actor = Actor.query.filter_by(nombre=data['nombre']).first()
      if actor is None:
        # Crea nuevo actor
        actor = Actor(**data)
        db.session.add(actor)
        db.session.commit()
        return {"result": actor_schema.dump(actor), "code": 200}

      return {"message": "Ya existe un actor con ese nombre", "code": 400, "actor": actor_schema.dump(actor)}, 400
    
    # Faltan PUT/PATCH y DELETE
    elif request.method == 'DELETE':
      return "DELETE"

    # Tal vez retornar error 500/404
    else:
      return "NADA!!!"
