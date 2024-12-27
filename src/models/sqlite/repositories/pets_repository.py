from typing import List
from sqlalchemy.orm.exc import NoResultFound 
from src.models.sqlite.entities.pets import Pet


class PetsRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
    
    def list_pets(self) -> List:
        with self.__db_connection as database:
            with self.__db_connection as database:
                try:
                    pets = database.session.query(Pet).all()
                    return pets
                except NoResultFound:
                    return []
    
    def delete_pets(self,name:str):
        with self.__db_connection as database:
            try:
                (
                    database.session.query(Pet)
                    .filter(Pet.name == name)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
