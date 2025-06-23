from flask import Blueprint, request, jsonify
from server.models import db
from server.models.user import User
from flask_jwt_extended import create_access_token
from server.models.guest import Guest

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()


    if not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required."}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username already exists."}), 409


    user = User(username=data['username'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "id": user.id,
        "username": user.username
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    
    if not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required."}), 400

    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid username or password."}), 401