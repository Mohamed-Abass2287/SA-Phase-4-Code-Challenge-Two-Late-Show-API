from server.models import db
from sqlalchemy.orm import validates, relationship

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = relationship("Appearance", backref="episode", cascade="all, delete")

    def __repr__(self):
        return f"<Episode {self.number} - {self.date}>"

    @validates('date')
    def validate_date(self, key, value):
        if not value:
            raise ValueError("Episode date is required.")
        return value

    @validates('number')
    def validate_number(self, key, value):
        if value is None or value < 1:
            raise ValueError("Episode number must be a positive integer.")
        return value