from flask import Blueprint, request, jsonify
from model import Cliente



cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes', methods=['GET'])
def obtener_clientes():
    clientes = Cliente.query.all()

    resultado = []
    for cliente in clientes:
        resultado.append({
            'rut_cli': cliente.rut_cli,
            'dv_cli': cliente.dv_cli,
            'nombre_cli': cliente.nombre_cli,
            'apat_cli': cliente.apat_cli,
            'amat_cli': cliente.amat_cli,
            'dir_cli': cliente.dir_cli,
            'fecha_nac_cli': cliente.fecha_nac_cli.strftime('%d-%m-%Y'),
            'email_cli': cliente.email_cli,
            'celular_cli': cliente.celular_cli,
            'contrasena_cli': cliente.contrasena_cli,
            'estado_suscripcion_cli': cliente.estado_suscripcion_cli,
            'id_com': cliente.id_com,
            'id_ciudad': cliente.id_ciudad,
            'id_region': cliente.id_region,
            'id_suscr': cliente.id_suscr
        })
    return jsonify({'clientes': resultado})
