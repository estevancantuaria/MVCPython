from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connections import db_connection_handler

from src.main.routes.pets_routes import pets_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pets_route_bp)