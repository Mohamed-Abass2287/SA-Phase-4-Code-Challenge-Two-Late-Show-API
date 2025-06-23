from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.guest import Guest


from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server.models import db

appearance_bp = Blueprint("appearances", __name__)

@appearance_bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()

    if not data or not all(k in data for k in ("rating", "guest_id", "episode_id")):
        return jsonify({"error": "Missing rating, guest_id, or episode_id"}), 400

    try:
      
        guest = Guest.query.get(data["guest_id"])
        episode = Episode.query.get(data["episode_id"])

        if not guest or not episode:
            return jsonify({"error": "Guest or Episode not found"}), 404

        if not (1 <= int(data["rating"]) <= 5):
            return jsonify({"error": "Rating must be between 1 and 5"}), 400

        appearance = Appearance(
            rating=data["rating"],
            guest_id=data["guest_id"],
            episode_id=data["episode_id"]
        )

        db.session.add(appearance)
        db.session.commit()

        return jsonify({
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500