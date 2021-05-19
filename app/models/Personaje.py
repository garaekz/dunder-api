from app import db, ma
from app.models.Actor import Actor, ActorSchema
from config.db import GUID
import uuid

class Personaje(db.Model):
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String(80), nullable=False)
    nombre_completo = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Boolean(), nullable=False, default=True)
    fecha_nacimiento = db.Column(db.Date(), nullable=True)
    descripcion = db.Column(db.Text(), nullable=True)
    actor_id = db.Column(GUID(), db.ForeignKey('actor.id'), nullable=False)
    actor = db.relationship(Actor, backref='personaje', lazy=True)

    def __repr__(self):
        return '<Personaje %r>' % self.nombre

class PersonajeSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Personaje

  actor = ma.Nested(ActorSchema)
  