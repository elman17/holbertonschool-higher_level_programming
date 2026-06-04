#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWR_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify(username, password):
    if username in users:
        return check_password_hash(users[username]["password"], password)
    return False


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity=username, additional_claims={"role": user("role")}
    )

    return jsonify({"access_token": token}), 200


@app.route("/jwt-proteced", methods=["GET"])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_required():
    current_user = get_jwt_identity()
    user = user.get(current_user)

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200


@jwt.invalid_token_loader
def expired_token_callback(header, payload):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run(port=5001, debug=True)

# print(users["user1"]["password"])
