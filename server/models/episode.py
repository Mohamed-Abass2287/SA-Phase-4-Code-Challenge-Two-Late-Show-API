from models import db

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    
    # Relationship with cascade deletion
    appearances = db.relationship(
        "Appearance",
        backref="episode",
        cascade="all, delete-orphan",
        lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "date": str(self.date),
            "number": self.number,
            "appearances": [appearance.to_dict() for appearance in self.appearances]
        }
