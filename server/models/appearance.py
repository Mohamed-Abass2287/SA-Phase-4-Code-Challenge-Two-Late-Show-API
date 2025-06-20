from models import db

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey("guest.id"), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey("episode.id"), nullable=False)
    guest = db.relationship("appearance", back_populates="appearances")
    
    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id
        }
