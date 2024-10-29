from flask import Flask, jsonify, request

from src.scripts.script import print_hello

app = Flask(__name__)

@app.route('/usage/<device_id>', methods=['GET'])
def get_device_usage(device_id):

    usage = {"device_id": device_id, "usage_percent": 75}  # Example static
    return jsonify(usage)


@app.route('/usage/all', methods=['GET'])
def get_all_device_usage():

    all_usage = [
        {"device_id": "1", "usage_percent": 75},
        {"device_id": "2", "usage_percent": 50}
    ]
    return jsonify(all_usage)

@app.route('/execute', methods=['POST'])
def execute_script():
    
    print_hello()
    return jsonify({"message": "Script executed successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
