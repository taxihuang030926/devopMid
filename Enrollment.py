import mysql.connector as mc
import init

def checkCourseNameConflict(S_ID, C_ID, db):
    cur = db.cursor()
    cur.execute("SELECT Course_Name FROM Courses WHERE Course_ID=%s;", (C_ID,))
    result = cur.fetchone()
    course_name = result[0]
    for i in range(1, 71):
        cur.execute("SELECT S%s FROM Enrolled_Table WHERE S_ID=%s;", (i, S_ID))
        result = cur.fetchone()
        course_iter = result[0]
        cur.execute("SELECT Course_Name FROM Courses WHERE Course_ID=%s;", (course_iter,))
        result = cur.fetchone()
        if result[0] == course_name or result is None:
            return False
    return True

def checkCourseTimeConflict(S_ID, C_ID, db):
    cur = db.cursor()
    cur.execute("SELECT Session_Time FROM Course_Session WHERE Course_ID=%s;", (C_ID,))
    results = cur.fetchall()
    for result in results:
        time = result[0]
        cur.execute("SELECT S%s FROM Enrolled_Table WHERE S_ID=%s;", (time, S_ID))
        result = cur.fetchone()
        course_iter = result[0]
        if course_iter != 0:
            return False
    return True

def checkCourseCredit(S_ID, C_ID, db):
    cur = db.cursor()
    cur.execute("SELECT Course_Credit FROM Courses WHERE Course_ID=%s;", (C_ID,))
    result = cur.fetchone()
    course_credit = result[0]
    cur.execute("SELECT Ttl_Credit FROM Student WHERE S_ID=%s;", (S_ID,))
    result = cur.fetchone()
    student_credit = result[0]
    if student_credit + course_credit > 25:
        return False
    return True

def checkEnrolled(S_ID, C_ID, db):
    cur = db.cursor()
    for i in range(1, 71):
        cur.execute("SELECT S%s FROM Enrolled_Table WHERE S_ID=%s;", (i, S_ID))
        result = cur.fetchone()
        if result[0] == C_ID:
            print(result[0])
            return False
    return True

def checkForEnrollment(S_ID, C_ID, db):
    if not checkCourseNameConflict(S_ID, C_ID, db):
        return False
    if not checkCourseTimeConflict(S_ID, C_ID, db):
        return False
    if not checkCourseCredit(S_ID, C_ID, db):
        return False
    if not checkEnrolled(S_ID, C_ID, db):
        return False
    return True

def enrollCourse(S_ID, C_ID, db):
    print("enrollCourse")
    if checkForEnrollment(S_ID, C_ID, db):
        cur = db.cursor()
        cur.execute("SELECT Course_Credit FROM Courses WHERE Course_ID=%s;", (C_ID,))
        result = cur.fetchone()
        course_credit = result[0]
        cur.execute("SELECT Ttl_Credit FROM Student WHERE S_ID=%s;", (S_ID,))
        result = cur.fetchone()
        student_credit = result[0]
        student_credit += course_credit
        cur.execute("UPDATE Student SET Ttl_Credit=%s WHERE S_ID=%s;", (student_credit, S_ID))
        db.commit()
        cur.execute("SELECT Session_Time FROM Course_Session WHERE Course_ID=%s;", (C_ID,))
        results = cur.fetchall()
        for result in results:
            time = result[0]
            cur.execute("UPDATE Enrolled_Table SET S%s=%s WHERE S_ID=%s AND S%s=0;", (time, C_ID, S_ID, time))
            db.commit()
        cur.close()
        return True
    return False