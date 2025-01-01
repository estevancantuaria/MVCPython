from src.controllers.pet_deleter_controller import PetDeleterController
from src.views.http_types.http_request import HttpRequest
from src.views.pet_deleter_view import PetDeleterView

def mockController(mocker):
    mock_repository = mocker.Mock()
    return PetDeleterController(mock_repository)

def test_delete(mocker):
    controller = mockController(mocker)
    view = PetDeleterView(controller)
    http_request = HttpRequest(param={"name": "Rex"})
    response = view.handle(http_request)
    assert response.status_code == 204