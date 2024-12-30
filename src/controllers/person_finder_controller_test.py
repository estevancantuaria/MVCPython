from .person_finder_controller import PersonFinderController

class MockPerson():
    def __init__(self, first_name: str, last_name: str, pet_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name

    
class MockPeopleRepository:
    def get_person_by_id(self) -> MockPerson:
        return MockPerson(
            first_name="John",
            last_name="Doe",
            pet_name="Rex",
        )

def test_find():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(123)
    
    expected_response = {
        "data": {
            "type": "person",
            "count": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "pet_name": "Rex",
            }
        }
    }
    
    print(response)
    print(expected_response)
    
    assert response == expected_response