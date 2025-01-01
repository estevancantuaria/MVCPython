from src.views.person_creator_view import PersonCreatorView
from src.controllers.person_creator_controller import PersonCreatorController
from src.views.http_types.http_request import HttpRequest

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass

def mockPersonCreatorController():
    return PersonCreatorController(MockPeopleRepository())

def test_create():
    controller = mockPersonCreatorController()
    view = PersonCreatorView(controller)
    http_request = HttpRequest(body={"first_name": "John", "last_name": "Doe", "age": 30, "pet_id": 1})
    response = view.handle(http_request)
    assert response.body == {"data": {"type": "person", "count": 1, "attributes": {"first_name": "John", "last_name": "Doe", "age": 30, "pet_id": 1}}}
