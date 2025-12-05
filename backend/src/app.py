from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/health")
def health():
    return jsonify({"status":"ok", "env": os.getenv("FLASK_ENV", "unknown")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
