from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="new record in the database")
def test__insert_attendee():
    event_id = "my-uuid"
    attendees_info = {
        "uuid": "my_uuid",
        "name": "attendee_name",
        "email": "email@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="...")
def test_get_attendee_badge_by_id():
    attendee_id = "my_uuid",
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)

    print(attendee)
    print(attendee.title)