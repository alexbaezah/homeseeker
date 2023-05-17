from flask import Blueprint, request, jsonify
from model import db, Region

region_bp = Blueprint('region', __name__)

@region_bp.route('/regiones', methods=['GET'])
def obtener_regiones():
    regiones = Region.query.all()
    resultado = []
    for region in regiones:
        resultado.append({'id_region': region.id_region, 'nombre_reg': region.nombre_reg})
    return jsonify({'regiones': resultado})

@region_bp.route('/regiones', methods=['POST'])
def crear_region():
    data = request.get_json()
    nueva_region = Region(id_region=data['id_region'], nombre_reg=data['nombre_reg'])
    db.session.add(nueva_region)
    db.session.commit()
    return jsonify({'mensaje': f'Región {nueva_region.nombre_reg} creada exitosamente.'})