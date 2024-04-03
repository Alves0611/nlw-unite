from flask import Blueprint

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/events", methods=["POST"])
def create_event():
    return jsonify({"olá": "mundo"}, 200)