from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.errors.error_handle import handle_errors
pets_route_bp = Blueprint('pets_routes', __name__)

@pets_route_bp.route('/pets', methods=['GET'])
def list_pets():
    try:
        http_request = HttpRequest()
        view = pet_lister_composer()
    
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code

@pets_route_bp.route('/pets/<name>', methods=['DELETE'])
def delete_pet(name):
    try:
        http_request = HttpRequest(param={'name': name})
        view = pet_deleter_composer()
        
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code
