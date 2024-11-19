import app
import init

def checkSession(S_ID, Course_ID, db):
    course_sessions = init.fetchCourseSession(Course_ID, db)
    enrolledtable = init.fetchEnrolledTable(S_ID, db)
    for session in course_sessions:
        session_time = session["Session_Time"]
        for i in range(1, 71):
            if int(enrolledtable[i]) == Course_ID:
                return False
    return True

def checkCourseNameConflict(Course_ID, S_ID, db):
    enrolled_course_ids = init.fetchEnrolledTable(S_ID, db)
    for i in range(1, 71):
        if int(enrolled_course_ids[i]) == Course_ID:
            return False
    return True

def checkCourseTimeConflict(S_ID, Course_ID, db):
    course_sessions = init.fetchCourseSession(Course_ID, db)
    enrolledtable = init.fetchEnrolledTable(S_ID, db)
    for session in course_sessions:
        session_time = session["Session_Time"]
        for i in range(1, 71):
            if int(enrolledtable[i]) == Course_ID:
                return False
    return True

def checkCourseCredit(S_ID, Course_ID, db):
    student = init.fetchStudent(S_ID, db)
    course = init.fetchCourse(Course_ID, db)
    if student["Ttl_Credit"] + course["Course_Credit"] > 25:
        return False
    return True