from flask import request
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="test")

def login(username, password):
    username = request.form['username']
    password = request.form['password']

    
