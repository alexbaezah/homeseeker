from flask import Blueprint, request, jsonify
from model import db, Comuna

comuna_bp = Blueprint('comuna', __name__)

@comuna_bp.route('/comunas', methods=['GET'])
def obtener_comunas():
    comunas = Comuna.query.all()

    resultado = []
    for com in comunas:
        comuna_data = {
            'id_com': com.id_com,
            'nom_com': com.nom_com,
            'id_ciudad': com.id_ciudad,
            'id_region': com.id_region
        }
        resultado.append(comuna_data)

    return jsonify({'comunas': resultado})