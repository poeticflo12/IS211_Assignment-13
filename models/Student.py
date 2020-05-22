from .database import Database as db_conn

class Student(db_conn):
    def __init__(self,data=None):
        if data is not None:
            self.firstname=data[0]
            self.lastname=data[1]
    
    def view_all_students(self):
        query="SELECT * FROM Student"
        result=self.fetch_all_rows(query)

        return result
    
    def addStudent(self):
        query = "INSERT INTO Student (first_name,last_name) VALUES (?,?)"
        values=[self.firstname,self.lastname]
        result=self.saving_or_editing(query,values)

    def delete_student(self,id):
        query= "DELETE FROM Student where id = (?)"
        result=self.delete_row(query,(id,))