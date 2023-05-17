from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model import db
from controllers.region import region_bp
from controllers.cliente import cliente_bp
from controllers.ciudad import ciudad_bp
from controllers.comuna import comuna_bp
from controllers.suscripcion import suscripcion_bp

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://INMOBILIARIA:1234@localhost:1521/XE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la instancia de SQLAlchemy
db.init_app(app)

# Registrar el blueprint de la región
app.register_blueprint(region_bp)

# Registrar el blueprint de cliente
app.register_blueprint(cliente_bp)

# Registrar el blueprint de ciudad
app.register_blueprint(ciudad_bp)

# Registrar el blueprint de comuna
app.register_blueprint(comuna_bp)

# Registrar el blueprint de suscripcion
app.register_blueprint(suscripcion_bp)

if __name__ == '__main__':
    app.run()