from src.controllers.person_creator_controller import PersonCreatorController
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorController) -> None:
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_info = http_request.body
        body_response = self.__controller.create(person_info)
        
        return HttpResponse(body=body_response)