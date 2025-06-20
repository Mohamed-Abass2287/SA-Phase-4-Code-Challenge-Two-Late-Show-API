from flask import Blueprint, request, jsonify
from models.appearance import Appearance
from models import db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint("appearance_bp", __name__)

@appearance_bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get("rating")
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")
    
    # Validate input
    if not (rating and guest_id and episode_id):
        return jsonify({"error": "rating, guest_id, and episode_id are required"}), 400
    
    try:
        rating = int(rating)
    except ValueError:
        return jsonify({"error": "Rating must be an integer"}), 400

    if rating < 1 or rating > 5:
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    new_appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(new_appearance)
    db.session.commit()
    
    return jsonify(new_appearance.to_dict()), 201
