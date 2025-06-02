" Unidad 5 - Ary Toro"

from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Paquete(db.Model):
    __tablename__='paquete'
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    numeroenvio = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.REAL,nullable=False)
    nomdestinatario = db.Column(db.VARCHAR(60), nullable=False)
    dirdestinatario = db.Column(db.VARCHAR(100), nullable=False)
    entregado = db.Column(db.Boolean, nullable=False)
    observaciones = db.Column(db.Text, nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'))


class Repartidor(db.Model):
    __tablename__='repartidor'
    id= db.Column(db.Integer,primary_key=True,nullable=False)
    numero= db.Column(db.Integer,nullable=False)
    nombre = db.Column(db.VARCHAR(60), nullable=False)
    dni = db.Column(db.VARCHAR(8), nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idpaquete= db.relationship('Paquete', backref='repartidor', cascade="all, delete-orphan", lazy='dynamic')


class Sucursal(db.Model):
    __tablename__='sucursal'
    id= db.Column(db.Integer,primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    provincia = db.Column(db.VARCHAR(30), nullable=False)
    localidad= db.Column(db.VARCHAR(30), nullable=False)
    direccion= db.Column(db.VARCHAR(60), nullable=False)
    idpaquete = db.relationship('Paquete', backref='sucursal', cascade="all, delete-orphan", lazy='dynamic')
    idrepartidor= db.relationship('Repartidor',backref='sucursal', cascade="all, delete-orphan", lazy='dynamic')
    idtransporte= db.relationship('Transporte',backref='sucursal', cascade="all, delete-orphan", lazy='dynamic')


class Transporte(db.Model):
    __tablename__='transporte'
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.Integer, nullable=False)
    fechahorasalida = db.Column(db.DateTime)
    fechahorallegada = db.Column(db.DateTime)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idpaquete = db.relationship('Paquete', backref='transporte', cascade="all, delete-orphan", lazy='dynamic')
