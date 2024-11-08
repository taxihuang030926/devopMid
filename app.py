from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    print(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)