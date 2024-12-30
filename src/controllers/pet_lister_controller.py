from typing import Dict, List
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import Pet

class PetListerController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository
        
    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response
    
    def __get_pets_in_db(self) -> List[Pet]:
        pets = self.__pets_repository.list_pets()
        return pets
    
    def __format_response(self, pets: List[Pet]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({"name": pet.name, "id": pet.id})
        
        return {
            "data": {
                "type": "pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }