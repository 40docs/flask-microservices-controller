from flask import Flask, request, jsonify
from services import math_service, echo_service

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"result": math_service.add(data['x'], data['y'])})

@app.route('/echo', methods=['GET'])
def echo():
    msg = request.args.get("msg", "")
    return jsonify({"echo": echo_service.echo_message(msg)})

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
