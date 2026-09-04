from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Student Management System Backend is Running!"


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
        email == "admin@gmail.com"
        and password == "1234"
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
    app.run(debug=True)