from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
__all__ = ['db', 'User', 'Guest', 'Episode', 'Appearance']