from ..dbinit import db
from datetime import datetime
from enum import Enum

class User(db.Document):
    email = db.StringField(required = True)
    
