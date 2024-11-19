import app
import init

def checkCredit(S_ID, Course_ID, db):
    student = init.fetchStudent(S_ID, db)
    course = init.fetchCourse(Course_ID, db)
    if student["Ttl_Credit"] - course["Course_Credit"] < 9:
        return False
    return True
