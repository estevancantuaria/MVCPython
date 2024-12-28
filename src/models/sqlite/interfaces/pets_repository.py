from abc import ABC, abstractmethod
from src.models.sqlite.entities.pets import Pet
from typing import List

class PetsRepositoryInterface(ABC):
    
    @abstractmethod
    def list_pets(self) -> List[Pet]:    
        pass
    
    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass
