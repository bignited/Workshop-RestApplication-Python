from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello, World!"

@app.route('/hello', methods=['POST'])
def hello_name():
    data = request.get_json()
    name = data.get('name', 'World')
    return jsonify(message=f"Hello, {name}")

if __name__ == '__main__':
    app.run(debug=True)