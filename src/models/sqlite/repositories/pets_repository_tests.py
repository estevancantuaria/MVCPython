from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import Pet
from .pets_repository import PetsRepository
from sqlalchemy.orm.exc import NoResultFound 

class Mockconnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Pet)],
                    [Pet(name="dog", type="dog"), Pet(name="toto", type="cat")]
                )
            ]
        )
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class MockconnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found
        
    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")
    
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    

def test_list_pets():
        mock_connection = Mockconnection()
        repo = PetsRepository(mock_connection)
        response = repo.list_pets()
        
        mock_connection.session.query.assert_called_once_with(Pet)
        mock_connection.session.all.assert_called_once()
        mock_connection.session.filter.assert_not_called()

        
        assert response[0].name == "dog"

def test_delete_pets():
        mock_connection = Mockconnection()
        repo = PetsRepository(mock_connection)
        repo.delete_pets("petName")
        
        mock_connection.session.query.assert_called_once_with(Pet)
        mock_connection.session.filter.assert_called_once_with(Pet.name == "petName")
        mock_connection.session.delete.assert_called_once()
        
def test_list_pets_no_result():
        mock_connection = MockconnectionNoResult()
        repo = PetsRepository(mock_connection)
        response = repo.list_pets()
        
        mock_connection.session.query.assert_called_once_with(Pet)
        mock_connection.session.all.assert_not_called()
        mock_connection.session.filter.assert_not_called()

        
        assert response == []

def test_delete_pets_error():
        mock_connection = MockconnectionNoResult()
        repo = PetsRepository(mock_connection)

        with pytest.raises(Exception):
            repo.delete_pets("petName")
        
        mock_connection.session.rollback.assert_called_once()
