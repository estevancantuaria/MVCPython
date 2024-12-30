import pytest
from src.models.sqlite.settings.connections import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository
# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interacao com o banco")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)

@pytest.mark.skip(reason="interacao com o banco") 
def test_delete_pets():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)

@pytest.mark.skip(reason="interacao com o banco") 
def test_insert_person():
    repo = PeopleRepository(db_connection_handler)
    repo.insert_person("João", "Silva", 30, 1)
    
@pytest.mark.skip(reason="interacao com o banco") 
def test_get_person():
    person_id = 1
    
    repo = PeopleRepository(db_connection_handler)
    repo.get_person_by_id(person_id)
