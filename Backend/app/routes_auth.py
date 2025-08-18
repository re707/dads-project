from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import AdminUser, db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    hashed_pw = generate_password_hash(password)
    user = AdminUser(username=username, password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Admin registered successfully!"})

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = AdminUser.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful!"})
    return jsonify({"error": "Invalid credentials"}), 401
