from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import Pet

class PeopleRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        with self.__db_connection as database:
            try:
                personData = PeopleTable(first_name=first_name, last_name=last_name, age=age, pet_id=pet_id)
                database.session.add(personData)
                database.session.commit()
            except:
                database.session.rollback()
                raise
    
    def get_person_by_id(self, person_id: int) -> PeopleTable:
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                    .query(PeopleTable)
                    .outerjoin(Pet, Pet.id == PeopleTable.pet_id)
                    .filter(PeopleTable.id == person_id)
                    .with_entities(PeopleTable.first_name, PeopleTable.last_name,Pet.name)
                    .one()
                )
                
                return person
            except NoResultFound:
                return None