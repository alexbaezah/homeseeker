from flask import Blueprint, jsonify
from model import db, Suscripcion

suscripcion_bp = Blueprint('suscripcion', __name__)

@suscripcion_bp.route('/suscripciones', methods=['GET'])
def obtener_suscripciones():
    suscripciones = Suscripcion.query.all()

    resultado = []
    for suscripcion in suscripciones:
        suscripcion_data = {
            'id_suscr': suscripcion.id_suscr,
            'fecha_inicio_sucr': suscripcion.fecha_inicio_sucr.strftime('%Y-%m-%d'),
            'fecha_fin_suscr': suscripcion.fecha_fin_suscr.strftime('%Y-%m-%d') if suscripcion.fecha_fin_suscr else None,
            'pagado': suscripcion.pagado,
            'id_tipo_suscr': suscripcion.id_tipo_suscr
        }
        resultado.append(suscripcion_data)

    return jsonify({'suscripciones': resultado})
