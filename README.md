# SA-Phase-4-Code-Challenge-Two-Late-Show-API

A Flask REST API for managing late-night show episodes, guest appearances, and user authentication. Built with PostgreSQL, Flask-JWT-Extended, and Flask-SQLAlchemy.

---

## 🔧 Technologies Used

- Python
- Flask
- Flask-JWT-Extended
- PostgreSQL
- SQLAlchemy
- Flask-Migrate
- Postman (for testing)
- JWT Authentication

---

## 📁 Project Structure

.
├── server/
│ ├── app.py
│ ├── config.py
│ ├── seed.py
│ ├── models/
│ │ ├── init.py
│ │ ├── user.py
│ │ ├── guest.py
│ │ ├── episode.py
│ │ └── appearance.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── auth_controller.py
│ │ ├── guest_controller.py
│ │ ├── episode_controller.py
│ │ └── appearance_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone: https://github.com/Mohamed-Abass2287/SA-Phase-4-Code-Challenge-Two-Late-Show-API
cd SA-Phase-4-Code-Challenge-Two-Late-Show-API
2. Install Dependencies
bash
Copy
Edit
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
3. PostgreSQL Setup
Make sure PostgreSQL is installed and running. Then:

bash
Copy
Edit
psql
CREATE DATABASE late_show_db;
\q
4. Configure Database URI
Edit server/config.py:

python
Copy
Edit
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:passward4127@localhost:5432/late_show_db"
🚀 Running the App
bash
Copy
Edit
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py  # optional///////
flask run
🔐 Authentication Flow
🔹 Register a User
POST /register

json
Copy
Edit
{
  "username": "mohaa",
  "password": "passward4127"
}
🔹 Login
POST /login

json
Copy
Edit
{
  "username": "mohaa",
  "password": "passward4127"
}
🔑 Response:

json
Copy
Edit
{
  "access_token": "eyJhbGciOi..."
}
Use this token as:

makefile
Copy
Edit
Authorization: Bearer <token>
📚 API Routes
Method	Endpoint	Auth?	Description
POST	/register	❌	Register a new user
POST	/login	❌	Log in and receive JWT token
GET	/episodes	❌	List all episodes
GET	/episodes/<id>	❌	Get single episode with appearances
DELETE	/episodes/<id>	✅	Delete an episode + appearances
GET	/guests	❌	List all guests
POST	/appearances	✅	Create an appearance

📬 Postman Collection
Import the file challenge-4-lateshow.postman_collection.json into Postman to test all endpoints.

✅ Submission Checklist
 MVC structure used

 PostgreSQL only (no SQLite)

 Models with validations

 Token-based JWT auth

 Protected routes implemented

 All routes tested via Postman

 GitHub repo linked and pushed

 README.md complete

