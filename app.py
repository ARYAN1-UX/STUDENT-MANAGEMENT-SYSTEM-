import os

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "login.html")


@app.route("/style.css")
def serve_css():
    return send_from_directory(BASE_DIR, "style.css")


@app.route("/script.js")
def serve_js():
    return send_from_directory(BASE_DIR, "script.js")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not email or not password or not role:
        return jsonify({
            "success": False,
            "message": "Please fill all fields."
        }), 400

    if (
        email == "ac3403020@gmail.com"
        and password == "1405"
        and role == "admin"
    ):
        return jsonify({
            "success": True,
            "message": "Admin login successful."
        })

    return jsonify({
        "success": False,
        "message": "Invalid email, password or role."
    }), 401


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)