import mysql.connector as mc
import init

def checkCredit(S_ID, Course_ID, db):
    cur = db.cursor()
    cur.execute("SELECT Course_Credit FROM Courses WHERE Course_ID=%s;", (Course_ID,))
    result = cur.fetchone()
    course_credit = result[0]
    cur.execute("SELECT Ttl_Credit FROM Student WHERE S_ID=%s;", (S_ID,))
    result = cur.fetchone()
    student_credit = result[0]
    if student_credit - course_credit < 9:
        return False
    return True

def checkCoursePrereq(Course_ID, db):
    course = init.fetchCourseData(Course_ID, db)
    prereq = course.prereq
    if prereq == 0:
        return True
    return False

def checkDrop(S_ID, Course_ID, db):
    if checkCredit(S_ID, Course_ID, db) and checkCoursePrereq(Course_ID, db):
        return True
    return False

def dropCourse(S_ID, Course_ID, db):
    print("dropCourse")
    if checkDrop(S_ID, Course_ID, db):
        cur = db.cursor()
        cur.execute("SELECT Course_Credit FROM Courses WHERE Course_ID=%s;", (Course_ID,))
        result = cur.fetchone()
        course_credit = result[0]
        cur.execute("SELECT Ttl_Credit FROM Student WHERE S_ID=%s;", (S_ID,))
        result = cur.fetchone()
        student_credit = result[0]
        student_credit -= course_credit
        cur.execute("UPDATE Student SET Ttl_Credit=%s WHERE S_ID=%s;", (student_credit, S_ID))
        db.commit()
        cur.execute("SELECT Session_Time FROM Course_Session WHERE Course_ID=%s;", (Course_ID,))
        results = cur.fetchall()
        for result in results:
            time = result[0]
            cur.execute("UPDATE Enrolled_Table SET S%s=0 WHERE S_ID=%s;", (time, S_ID))
            db.commit()


        cur.close()
        return True
    return False