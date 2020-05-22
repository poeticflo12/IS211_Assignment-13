from app import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)  

    # def get_id(self):
    #     # returns the user e-mail. not sure who calls this
    #     return self.username

    # def is_authenticated(self):
    #     return self.authenticated

    # def is_anonymous(self):
    #     # False as we do not support annonymity
    #     return False

    #constructor
    def __init__(self,username=None, password=None):
    
        self.username = username
        self.password = password
        self.authenticated = True 