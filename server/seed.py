from server.extensions import db
from server.models.episode import Episode
from server.models.guest import Guest

def seed_data():
    # Add Guests
    guest1 = Guest(name="Stephen King", occupation="Author")
    guest2 = Guest(name="Taylor Swift", occupation="Musician")
    guest3 = Guest(name="Serena Williams", occupation="Athlete")

    # Add Episodes
    episode1 = Episode(date="2025-06-01", number=1)
    episode2 = Episode(date="2025-06-02", number=2)
    episode3 = Episode(date="2025-06-03", number=3)

    db.session.add_all([guest1, guest2, guest3, episode1, episode2, episode3])
    db.session.commit()
    print("Seeded guests and episodes.")

if __name__ == "__main__":
    from server.app import create_app
    app = create_app()
    with app.app_context():
        seed_data()