from flask import Flask, request, jsonify, render_template, url_for, redirect, session
from flask import request
import MySQLdb
import sys
app = Flask(__name__)

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="student")

username = ""
password = ""

def login1(username, password):
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    return result is not None

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if login1(username, password):
            session['username'] = username
            flash('登入成功', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('登入失敗，請檢查您的 NID 和密碼', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)