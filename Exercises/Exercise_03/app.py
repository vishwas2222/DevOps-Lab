
from flask import Flask, jsonify
from datetime import datetime, timezone
import os
import random

app = Flask(__name__)

PRODUCTS = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Smartwatch",
    "Keyboard"
]

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Flash Sale!",
        "pod": os.getenv("HOSTNAME", "local"),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/buy")
def buy():
    return jsonify({
        "message": "Purchase successful!",
        "product": random.choice(PRODUCTS),
        "user": f"user-{random.randint(1000, 9999)}",
        "pod": os.getenv("HOSTNAME", "local"),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "pod": os.getenv("HOSTNAME", "local")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
