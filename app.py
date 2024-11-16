from flask import Flask, request, jsonify, render_template, url_for, redirect, session
import mysql.connector as mc  # type: ignore
import login

app = Flask(__name__)
username = ""
password = ""

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)