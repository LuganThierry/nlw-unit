import pytest
from .attendees_repository import AttendesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco")
def test_insert_attendee():
    event_id = "teste123"
    attendees_info = {
        "uuid": "meu_uuid_attendee",
        "name": "attendee name",
        "email": "email@email.com",
        "event_id": event_id
    }

    attendees_repository = AttendesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="...")
def test_get_attendee__badge_by_id():
    attendee_id = "meu_uuid_attendee"
    attendee_repository = AttendesRepository()
    attendee = attendee_repository.get_attendee__badge_by_id(attendee_id)

    print(attendee)