from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.guest import Guest

from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models import db

episode_bp = Blueprint("episodes", __name__)

@episode_bp.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {"id": e.id, "date": e.date, "number": e.number} for e in episodes
    ]), 200

@episode_bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [
            {"guest_id": a.guest_id, "rating": a.rating}
            for a in episode.appearances
        ]
    }), 200

@episode_bp.route("/episodes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify(message=f"Episode {id} deleted successfully."), 200