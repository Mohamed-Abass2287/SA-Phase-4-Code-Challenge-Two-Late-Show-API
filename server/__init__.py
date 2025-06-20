from flask import Flask
from flask_migrate import Migrate
from .models import db

app = Flask(__name__)
# migrate = Migrate(app, db)

