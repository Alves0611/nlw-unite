from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendesHandler

attendees_route_bp = Blueprint("attendees_route", __name__)

@attendees_route_bp.route("/events/<event_id>/register", methods=["POST"])
def create_attendess(event_id): 
    attendes_handler = AttendesHandler()
    http_request = HttpRequest(param={"event_id": event_id}, body=request.json)                                                  
                                                                
    http_response = attendes_handler.registry(http_request)
    return jsonify(http_response.body), http_response.status_code     


@attendees_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendess_batch(attendee_id): 
    attendes_handler = AttendesHandler()
    http_request = HttpRequest(param={"attendee_id": attendee_id})
                                                                
    http_response = attendes_handler.find_attendee_badge(http_request)
    return jsonify(http_response.body), http_response.status_code     