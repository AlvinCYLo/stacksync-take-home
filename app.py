from flask import Flask, request, jsonify
import json
from libraries import libraries

app = Flask(__name__)

#pipenv run flask run -h localhost -p 8080
#https://www.programiz.com/python-programming/methods/built-in/exec

@app.route("/execute", methods=["POST"])
def execute():
    env = dict([(lib, locals().get(lib, None)) for lib in libraries]) 
    try:
        data = request.json
        script = data.get('script')
        exec(script, {"__builtins__": None}, env)
        resp = env['main']()
        json.loads(resp)
        return jsonify(resp)
    
    except Exception as e:
        print(e)
        return e