from flask import request
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="test")

def login1(username, password):
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    return result is not None    
