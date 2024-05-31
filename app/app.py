from flask import Flask, request, jsonify
import json
from libraries import libraries

app = Flask(__name__)

#https://github.com/docker/awesome-compose/tree/master/flask

@app.route("/execute", methods=["POST"])
def execute():
    try:
        data = request.json
        script = validate_data(data)
        response = execute_script(script)
        return validate_response(response)
    except Exception as e:
        print(e)
        return Exception(e)


def validate_data(data):
    try:
        script = data.get('script')
        if not script:
            raise Exception("Data missing")
        return script
         
    except Exception as e:
        print(e)
        raise Exception("Invalid payload structure", e)


#https://www.programiz.com/python-programming/methods/built-in/exec
def execute_script(script):
    env = dict([(lib, locals().get(lib, None)) for lib in libraries]) 
    try:
        exec(script, {"__builtins__": None}, env)
        resp = env['main']()
        return resp
    
    except Exception as e:
        print(e)
        raise Exception('Error executing script', e)


def validate_response(resp):
    try:
        validated = json.loads(resp)
        return jsonify(validated)
    except Exception as e:
        raise Exception("Invalid response structure", e)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)