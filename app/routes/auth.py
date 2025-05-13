from flask import Blueprint, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/token', methods=['GET'])
def generate_token():
    fake_user_id = 42  # ID d’exemple
    access_token: str = create_access_token(identity=fake_user_id)
    return jsonify(access_token=access_token)
@auth_bp.route('/', methods=['GET'])
def index():
    return jsonify(message="Bienvenue dans l'API !")
