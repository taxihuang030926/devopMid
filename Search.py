import MySQLdb
import mysql.connector as mc

def searchUser(db, username, password):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Student WHERE S_ID=%s AND S_pwd=%s;", (username, password))
    result = cursor.fetchone()
    cursor.close()
    print(result)

    return result