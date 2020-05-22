from .database import Database as db_conn
class StudentMarks(db_conn):
    def __init__(self,data=None):
        if data is not None:
            self.studentmarks=data[0]
            self.student_id=data[1]
            self.quiz_id=data[2]
        
    def viewall(self):
        query="""select sm.id, sm.marks , s.first_name, s.last_name, q.subject from Student_Result sm 
        INNER JOIN Student s on sm.student_id=s.id 
        INNER JOIN Quizzes q on sm.quiz_id=q.id;"""
        result=self.fetch_all_rows(query)
        return result

    def addmarks(self):
        query="INSERT INTO Student_Result (student_id, quiz_id, marks) values (?,?,?)"
        result=self.saving_or_editing(query,(self.student_id,self.quiz_id,self.studentmarks))

    def single_student(self,id):
        query=query="""select sm.id, sm.marks , s.first_name, s.last_name, q.subject, s.id from Student_Result sm 
        INNER JOIN Student s on sm.student_id=s.id 
        INNER JOIN Quizzes q on sm.quiz_id=q.id
        where sm.id=(?);"""
        result=self.fetch_single_row(query,[id])
        return result

    def delete_marks(self,id):
        query="DELETE FROM Student_Result where id = (?)"
        result=self.delete_row(query,(id,))
        return result