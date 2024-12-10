from flask import Flask, request, jsonify

app = Flask(__name__)

friends = ['Alice', 'Bob', 'Charlie']   

@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello, World!"

@app.route('/hello', methods=['POST'])
def hello_name():
    data = request.get_json()
    name = data.get('name', 'World')
    return jsonify(message=f"Hello, {name}")

@app.route('/friends', methods=['GET'])
def hello_friends():
    return friends

@app.route('/friend', methods=['POST'])
def new_friends():
    data = request.get_json()
    name = data.get('name')
    friends.append(name)
    return jsonify(message=f"Welcome, {name}")

@app.route('/friend/<name>', methods=['DELETE'])
def remove_friend(name):
    friends.remove(name)
    return jsonify(message=f"Bye, {name}")

@app.route('/friend/<name>', methods=['PUT'])
def update_friend(name):
    data = request.get_json()
    new_name = data.get('name')
    if name not in friends:
        return jsonify(message=f"{name} not found")
    friends.remove(name)
    friends.append(new_name)
    return jsonify(message=f"Updated, {name} to {new_name}")

if __name__ == '__main__':
    app.run(debug=True)