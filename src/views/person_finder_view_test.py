from src.controllers.person_finder_controller import PersonFinderController
from src.views.http_types.http_request import HttpRequest
from src.views.person_finder_view import PersonFinderView

class MockPerson():
    def __init__(self, first_name: str, last_name: str, pet_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name

    
class MockPeopleRepository:
    def get_person_by_id(self, person_id: int) -> MockPerson:  # pylint: disable=unused-argument
        return MockPerson(
            first_name="John",
            last_name="Doe",
            pet_name="Rex",
        )

def mockPersonFinderController():
    return PersonFinderController(MockPeopleRepository())

def test_find():
    controller = mockPersonFinderController()
    view = PersonFinderView(controller)
    http_request = HttpRequest(param={"person_id": 1})
    response = view.handle(http_request)
    assert response.body == {"data": {"type": "person", "count": 1, "attributes": {"first_name": "John", "last_name": "Doe", "pet_name": "Rex"}}}
