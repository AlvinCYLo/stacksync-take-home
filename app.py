from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def home(json):
    script = request.json
    print(json)
    print(script)