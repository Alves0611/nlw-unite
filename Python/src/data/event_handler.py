import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()

    def register(self, http_request) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)

        return HttpResponse(
            body={ "eventId": body["uuid"]},
            status_code=200
        )
    

    def find_by_id(self, http_request: HttpResponse ) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event = self.__events_repository.get_event_by_id(event_id)
        if not event: raise Exception("event not found")

        event_attendees_count = self.__events_repository.count_event_attendesses(event_id)

        return HttpResponse(
            body = {
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "description": event.description,
                    "location": event.location,
                    "start_date": event.start_date,
                    "end_date": event.end_date,
                    "maximum_attendees": event.maximum_attendees,
                    "attendeesAmount": event_attendees_count["attendeesAmount"]
                }
            },
            status_code=200
        )