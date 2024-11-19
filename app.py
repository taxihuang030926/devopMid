<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template, url_for, redirect, session, flash
import mysql
import MySQLdb
import mysql.connector as mc 
import Search, Enrollment, Drop
from init import fetchStudentData, fetchCourseData, fetchCourseSession, fetchEnrolledTable, fetchCourseSession
import sys
=======
from flask import Flask, request, jsonify, render_template, url_for, redirect, session
>>>>>>> 9e6ed6fe643dfcf6170a7f79fa95d50fe2ae277b

app = Flask(__name__)
app.secret_key = b'5aBMRhcy'

db = mc.connect(host="0.0.0.0", port=3306, user="admint", password="12341234", database="devopMid")
cursor = db.cursor()

username = ""
password = ""

# login 
@app.route('/')
def index():
    if 'username' in session:
        render_template('dashboard.html', usernameKept=session['username'])
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if(Search.searchUser(db, username, password)):
        session['username'] = username
        render_template('dashboard.html', usernameKept=session['username'])
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username or password')
        render_template('index.html')
        return redirect(url_for('index'))

# dashboard 
@app.route('/dashboard')
def dashboard():
    print(username)
    return render_template('dashboard.html', usernameKept=session['username'])

@app.route('/handle_course', methods=['POST'])
def handle_course():
    course_id = request.form['course_id']
    S_ID = session.get('username') 
    # if(Search.searchCourse(db, course_id)):

    return render_template('dashboard.html', usernameKept=session['username'])
    

@app.route('/logout')
def logout():
    username = ""
    password = ""
    session.clear()
    print("session killed")
    render_template('index.html')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)