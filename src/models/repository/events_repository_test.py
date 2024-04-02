import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco")
def test_inser_event():
    event = {
        "uuid": "teste123",
        "title": "o título do meu evento de teste00",
        "slug": "o slogan do meu evento de teste00",
        "maximum_attendees": 22
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)

    print(response)

# @pytest.mark.skip(reason="Desnecessário")
def test_get_event_by_id():
    event_id = "teste123"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)

    print(response)