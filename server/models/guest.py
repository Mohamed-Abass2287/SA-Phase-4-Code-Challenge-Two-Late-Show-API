from server.models import db
from sqlalchemy.orm import validates
from server.models.appearance import Appearance

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

  
    appearances = db.relationship('Appearance', backref='guest', cascade="all, delete")

    def __repr__(self):
        return f"<Guest {self.name}>"

    @validates('name', 'occupation')
    def validate_strings(self, key, value):
        if not value or not isinstance(value, str):
            raise ValueError(f"{key} must be a non-empty string.")
        return value