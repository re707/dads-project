from flask import Blueprint, request, jsonify
from .models import Event, db
import os

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/add-event", methods=["POST"])
def add_event():
    title = request.form.get("title")
    description = request.form.get("description")
    image = request.files.get("image")

    filename = None
    if image:
        filename = image.filename
        path = os.path.join("backend/uploads", filename)
        image.save(path)

    new_event = Event(title=title, description=description, image=filename)
    db.session.add(new_event)
    db.session.commit()

    return jsonify({"message": "Event added successfully!"}), 201
