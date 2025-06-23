from flask_bcrypt import Bcrypt
from datetime import date
from server.app import create_app
from server.models import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

bcrypt = Bcrypt()
app = create_app()

with app.app_context():
    print("Seeding database...")

    db.drop_all()
    db.create_all()

   
    password_hash = bcrypt.generate_password_hash('admin123').decode('utf-8')
    user1 = User(username="admin", password_hash=password_hash)

   
    guest1 = Guest(name="Osman Fahiye", occupation="Comedian")
    guest2 = Guest(name="Ali", occupation="Developer")
    guest3 = Guest(name="Julius", occupation="Mentor")

 
    ep1 = Episode(date=date(2023, 9, 1), number=101)
    ep2 = Episode(date=date(2023, 9, 2), number=102)
    ep3 = Episode(date=date(2023, 9, 3), number=103)


    app1 = Appearance(rating=5, guest=guest1, episode=ep1)
    app2 = Appearance(rating=4, guest=guest2, episode=ep1)
    app3 = Appearance(rating=5, guest=guest3, episode=ep2)
    app4 = Appearance(rating=3, guest=guest2, episode=ep3)

  
    db.session.add_all([
        user1,
        guest1, guest2, guest3,
        ep1, ep2, ep3,
        app1, app2, app3, app4
    ])
    db.session.commit()

    print("Seeding complete!")