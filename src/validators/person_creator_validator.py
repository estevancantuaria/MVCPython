from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_umprocessable_entity import HttpUnprocessableEntityError

def person_creator_validator(request:HttpRequest) -> None:
    
    
    #     first_name = person_info['first_name']
    # last_name = person_info['last_name']
    # age = person_info['age']
    # pet_id = person_info['pet_id']
    class BodyData(BaseModel):
        first_name: constr(min_length=1) #type: ignore
        last_name: constr(min_length=1) #type: ignore
        age: int
        pet_id: int

    try:
        BodyData(**request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
