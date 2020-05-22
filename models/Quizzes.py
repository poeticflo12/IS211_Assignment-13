from .database import Database as db_conn

class Quizzes(db_conn):
    def __init__(self, data=None):
        if data is not None:
            self.subject=data[0]
            self.question=data[1]
            self.date=data[2]
    
    def view_all_quizzes(self):
        query="SELECT * FROM Quizzes"

        result=self.fetch_all_rows(query)
        return result

    def add_quiz(self):
        query="INSERT INTO Quizzes (subject,quiz_date,no_questions) values (?,?,?)"

        result=self.saving_or_editing(query,[self.subject,self.date,self.question])
        return result
    
    def delete_quiz(self,id):
        query="DELETE FROM Quizzes where id = (?)"
        result=self.delete_row(query,(id,))
        return result