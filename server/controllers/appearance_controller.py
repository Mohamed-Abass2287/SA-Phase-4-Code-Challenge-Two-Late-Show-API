from flask import Blueprint, request, jsonify
from models.appearance import Appearance
from app import db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get("rating")
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")

    if rating is None or guest_id is None or episode_id is None:
        return {"error": "rating, guest_id, and episode_id are required"}, 400
    
    if not (1 <= rating <= 5):
        return {"error": "rating must be between 1 and 5"}, 400

    appearance = Appearance(
        rating=rating,
        guest_id=guest_id,
        episode_id=episode_id
    )
    db.session.add(appearance)
    db.session.commit()
    return {
        "id": appearance.id,
        "rating": appearance.rating,
        "guest_id": appearance.guest_id,
        "episode_id": appearance.episode_id
    }, 201