from src.models.sqlite.entities.pets import Pet
from src.controllers.pet_lister_controller import PetListerController
from src.views.pet_lister_view import PetListerView
from src.views.http_types.http_request import HttpRequest

class MockPetsRepository:
    def list_pets(self):
        return [
            Pet(name="Rex", id=123),
            Pet(name="Bella", id=456),
        ]

def mockController():
    return PetListerController(MockPetsRepository())

def test_list():
    controller = mockController()
    view = PetListerView(controller)
    http_request = HttpRequest()
    response = view.handle(http_request)
    assert response.status_code == 200
    assert response.body == {"data": {"type": "pets", "count": 2, "attributes": [{"name": "Rex", "id": 123}, {"name": "Bella", "id": 456}]}}