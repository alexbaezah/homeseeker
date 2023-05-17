from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()


class Region(db.Model):
    __tablename__ = 'REGION'
    id_region = db.Column(db.Integer, primary_key=True)
    nombre_reg = db.Column(db.String(80), nullable=False)
    
    

class Ciudad(db.Model):
    __tablename__ = 'CIUDAD'
    id_ciudad = db.Column(db.Integer, primary_key=True)
    nom_ciud = db.Column(db.String(80), nullable=False)
    id_region = db.Column(db.Integer, db.ForeignKey('REGION.id_region'), nullable=False)



class Comuna(db.Model):
    __tablename__ = 'COMUNA'
    id_com = db.Column(db.Integer, primary_key=True)
    nom_com = db.Column(db.String(100), nullable=False)
    id_ciudad = db.Column(db.Integer, db.ForeignKey('CIUDAD.id_ciudad'))
    id_region = db.Column(db.Integer, db.ForeignKey('REGION.id_region'))

 


class TipoSuscripcion(db.Model):
    __tablename__ = 'TIPO_SUSCRIPCION'

    id_tipo_suscr = db.Column(db.Integer, primary_key=True)
    nombre_tipo_suscr = db.Column(db.String(100), nullable=False)
    costo_tipo_suscr = db.Column(db.Integer)

class Suscripcion(db.Model):
    __tablename__ = 'SUSCRIPCION'

    id_suscr = db.Column(db.Integer, primary_key=True)
    fecha_inicio_sucr = db.Column(db.Date, nullable=False)
    fecha_fin_suscr = db.Column(db.Date)
    pagado = db.Column(db.String(1), default='I')
    id_tipo_suscr = db.Column(db.Integer, db.ForeignKey('TIPO_SUSCRIPCION.id_tipo_suscr'))

   

class Cliente(db.Model):
    __tablename__ = 'CLIENTE'
    rut_cli = db.Column(db.String(8), primary_key=True)
    dv_cli = db.Column(db.String(1), nullable=False)
    nombre_cli = db.Column(db.String(80), nullable=False)
    apat_cli = db.Column(db.String(80), nullable=False)
    amat_cli = db.Column(db.String(80), nullable=False)
    dir_cli = db.Column(db.String(100), nullable=False)
    fecha_nac_cli = db.Column(db.Date, nullable=False)
    email_cli = db.Column(db.String(100), nullable=False)
    celular_cli = db.Column(db.String(12), nullable=False)
    contrasena_cli = db.Column(db.String(6), nullable=False)
    estado_suscripcion_cli = db.Column(db.String(1), default='I')
    id_com = db.Column(db.Integer, db.ForeignKey('COMUNA.id_com'))
    id_ciudad = db.Column(db.Integer, db.ForeignKey('CIUDAD.id_ciudad'))
    id_region = db.Column(db.Integer, db.ForeignKey('REGION.id_region'))
    id_suscr = db.Column(db.Integer, db.ForeignKey('SUSCRIPCION.id_suscr'), nullable=True)

    suscripcion = db.relationship('Suscripcion', backref='cliente', lazy=False)

