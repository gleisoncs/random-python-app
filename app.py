from flask import Flask, jsonify, request
import os
import uuid
from datetime import datetime
import logging

app = Flask(__name__)

logging.basicConfig(filename='/var/log/app/access.log', level=logging.INFO, format='%(asctime)s %(message)s')

@app.route("/")
def random_guid():
    guid = str(uuid.uuid4())
    
    logging.info(f"guid: {guid}, ip: {request.remote_addr}")

    pod_name = os.getenv("HOSTNAME", "unknown-pod")
    node_name = os.getenv("NODE_NAME", "unknown-node")
    current_time = datetime.now().isoformat()
    
    response = {
        "current_time": current_time,
        "guid": guid,
        "pod_name": pod_name,
        "node_name": node_name
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
