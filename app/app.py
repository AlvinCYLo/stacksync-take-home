from flask import Flask, request, jsonify
import json
import subprocess

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def execute():
    try:
        data = request.json
        script = validate_data(data)
        response = execute_script(script)
        print(response)
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


def execute_script(script):
    script_path = 'script.py'
    try:
        with open(script_path, 'w') as f:
            f.write(script)
            f.close()
            
        command = ['nsjail', '--config', 'nsjail.cfg', '--detect_cgroupv2', '--cgroup_cpu_ms_per_sec', '100', '--', '../usr/local/bin/python', script_path]
        result = subprocess.run(command, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return result.stderr.strip()
    
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