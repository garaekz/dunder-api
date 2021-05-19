from app import db, ma
from config.db import GUID
import uuid



class Actor(db.Model):
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String(80), nullable=False, unique=True)
    nombre_completo = db.Column(db.String(80), nullable=False)
    fecha_nacimiento = db.Column(db.Date(), nullable=True)
    descripcion = db.Column(db.Text(), nullable=True)

    def __repr__(self):
        return '<Actor %r>' % self.nombre

class ActorSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Actor