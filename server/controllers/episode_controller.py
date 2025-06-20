from flask import Blueprint, jsonify, request
from models.episode import Episode
from models import db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint("episode_bp", __name__)

@episode_bp.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([ep.to_dict() for ep in episodes]), 200

@episode_bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify(episode.to_dict()), 200

@episode_bp.route("/episodes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": "Episode and its appearances deleted."}), 200
