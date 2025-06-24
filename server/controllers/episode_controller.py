from flask import Blueprint, jsonify, request
from models.episode import Episode
from models.appearance import Appearance
from flask_jwt_extended import jwt_required
from app import db

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.order_by(Episode.date.desc()).all()
    result = []
    for ep in episodes:
        result.append({
            "id": ep.id,
            "date": ep.date.isoformat(),
            "number": ep.number
        })
    return jsonify(result), 200


@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    appearances_list = []
    for a in appearances:
        appearances_list.append({
            "id": a.id,
            "rating": a.rating,
            "guest_id": a.guest_id,
        })
    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": appearances_list
    }), 200


@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)  
    db.session.commit()
    return {"message": f"Episode {id} deleted"}, 200