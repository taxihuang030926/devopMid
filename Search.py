import MySQLdb
import mysql.connector as mc

def searchUser(db, username, password):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Student WHERE S_ID=%s AND S_pwd=%s;", (username, password))
    result = cursor.fetchone()
    cursor.close()
    return result

def searchCourse(db, course_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Courss WHERE Course_ID=%s;", (course_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

def searchSession(db, course_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Course_Session WHERE Course_ID=%s;", (course_id,))
    result = cursor.fetchall()
    cursor.close()
    return result

def searchEnrolled(db, S_ID):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Enrolled_Table WHERE S_ID=%s;", (S_ID,))
    result = cursor.fetchone()
    cursor.close()
    return result

def searchStudentClass(db, S_ID):
    cursor = db.cursor()
    cursor.execute("SELECT Class FROM Student WHERE S_ID=%s;", (S_ID,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None
