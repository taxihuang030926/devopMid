from flask import Flask, request, jsonify, render_template, url_for, redirect, session, flash
import mysql
import MySQLdb
import mysql.connector as mc 
import Search, Enrollment, Drop
import sys

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
        return render_template('dashboard.html')
    else:
        return render_template('index.html')

@app.route('/', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if(Search.searchUser(db, username, password)):
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username or password')
        return redirect(url_for('login'))

# dashboard 
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', username=username)

@app.route('/dashboard', methods=['POST'])
def logout():
    username = ""
    password = ""
    session.clear()
    return redirect(url_for('/'))


if __name__ == '__main__':
    app.run(debug=True)