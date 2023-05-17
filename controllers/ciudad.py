from flask import Blueprint, request, jsonify
from model import db, Ciudad

ciudad_bp = Blueprint('ciudad', __name__)

@ciudad_bp.route('/ciudades', methods=['GET'])
def obtener_ciudades():
    ciudades = Ciudad.query.all()

    resultado = []
    for ciudad in ciudades:
        ciudad_data = {
            'id_ciudad': ciudad.id_ciudad,
            'nom_ciud': ciudad.nom_ciud,
            'id_region': ciudad.id_region
        }
        resultado.append(ciudad_data)

    return jsonify({'ciudades': resultado})