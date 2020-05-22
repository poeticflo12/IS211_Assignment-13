import sqlite3
from sqlite3 import Error

class Database:
    
    def __init__(self):
        """"Initialize the database connection"""
        try:
            conn=sqlite3.connect("./hw13.db")
            cur=conn.cursor()
            # global conn,cur
            
        except Error as e:
            print(e)
    def fetch_single_row(self,query,data):
        """Fetches a single row in a table"""
        conn=sqlite3.connect("./hw13.db")
        cur=conn.cursor()
        cur.execute(query,data)
        fetchedRow=cur.fetchone()
        return fetchedRow
    
    def saving_or_editing(self,query,data):
        """Saves or edits data in the database"""
        conn=sqlite3.connect("./hw13.db")
        cur=conn.cursor()
        cur.execute(query,data)
        conn.commit()
    
    def fetch_all_rows(self,query):
        """Fetches all rows in a table"""
        conn=sqlite3.connect("./hw13.db")
        cur=conn.cursor()
        cur.execute(query)
        all_rows=cur.fetchall()
        return all_rows
    
    def delete_row(self,query,data):
        """Deletes a row in a table"""
        conn=sqlite3.connect("./hw13.db")
        cur=conn.cursor()
        cur.execute(query,data)
        conn.commit()