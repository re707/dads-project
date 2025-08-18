from flask import Blueprint, request, jsonify
from .models import ContactMessage, db

main_bp = Blueprint("main", __name__)

@main_bp.route("/api/contact", methods=["POST"])
def contact():
    data = request.form
    new_msg = ContactMessage(
        name=data.get("name"),
        email=data.get("email"),
        message=data.get("message")
    )
    db.session.add(new_msg)
    db.session.commit()
    return jsonify({"message": "Your message has been sent successfully!"}), 201
