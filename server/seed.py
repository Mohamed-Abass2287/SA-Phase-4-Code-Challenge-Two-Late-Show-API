from app import create_app
from models import db
from models.guest import Guest
from models.episode import Episode
from datetime import date

app = create_app()
app.app_context().push()

# Initialize the db object with the app instance
db.init_app(app)

# Delete existing data if necessary
with app.app_context():
    db.drop_all()
    db.create_all()

# Create sample guests
guest1 = Guest(name="Morgan", occupation="Comedian")
guest2 = Guest(name="Alex", occupation="Musician")

# Create sample episodes
episode1 = Episode(date=date(2025, 6, 20), number=1)
episode2 = Episode(date=date(2025, 6, 27), number=2)

db.session.add_all([guest1, guest2, episode1, episode2])
db.session.commit()

print("Seed data inserted.")