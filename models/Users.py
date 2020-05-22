from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin
from .database import Database as db_conn
import sqlite3
from sqlite3 import Error   


class User(db_conn,UserMixin):
    def __init__(self, username, password):
        self.username=username
        self.password=password

    def get_user(self):
        """Adding a question to database"""
        query="SELECT * FROM User WHERE username=? and password=?"
        result=self.fetch_single_row(query,(self.username,self.password))
        # print(result)
        return result

    # def set_password(self):
    #     self.password_hash = generate_password_hash(self.password)
    
    def get_id(self):
        """get user by id"""
        return str(self.username)

    def check_password(self, password):
        return check_password_hash(self.password_hash, self.password)