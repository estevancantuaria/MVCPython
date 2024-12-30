from src.models.sqlite.entities.pets import Pet
from src.controllers.pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            Pet(name="Rex", id=123),
            Pet(name="Bella", id=456),
        ]
        
def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()
    
    expected_response = {
        "data": {
            "type": "pets",
            "count": 2,
            "attributes": [{"name": "Rex", "id": 123}, {"name": "Bella", "id": 456}]
        }
    }
    
    assert response == expected_response
