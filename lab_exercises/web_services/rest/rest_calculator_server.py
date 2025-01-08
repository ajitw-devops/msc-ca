from flask import Flask, jsonify, request

app = Flask(__name__)

# Route for addition
@app.route('/add', methods=['POST'])
def add():
    data = request.json
    intA = data.get('intA')
    intB = data.get('intB')
    result = intA + intB
    return jsonify({'result': result})

# Route for subtraction
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    intA = data.get('intA')
    intB = data.get('intB')
    result = intA - intB
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
