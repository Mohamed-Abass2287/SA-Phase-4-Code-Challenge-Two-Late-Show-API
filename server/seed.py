# server/seed.py

from server.extensions import db
from server.models.guest import Guest
from server.models.episode import Episode
from server.app import create_app


def seed_guests():
    guests = [
        Guest(name="Stephen King", occupation="Author"),
        Guest(name="Taylor Swift", occupation="Musician"),
        Guest(name="Serena Williams", occupation="Athlete"),
    ]
    db.session.add_all(guests)
    print(f"Seeded {len(guests)} guests.")


def seed_episodes():
    episodes = [
        Episode(date="2025-06-01", number=1),
        Episode(date="2025-06-02", number=2),
        Episode(date="2025-06-03", number=3),
    ]
    db.session.add_all(episodes)
    print(f"Seeded {len(episodes)} episodes.")


def run_seeding():
    seed_guests()
    seed_episodes()
    db.session.commit()
    print("✅ Seeding complete!")


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        run_seeding()
