from .database_connector import DatabaseConnector
from .interfaces.database_repository import DatabaseRepositoryInterface


class DatabaseRepository(DatabaseRepositoryInterface):

    @classmethod
    def insert_artist(cls, data: dict) -> None:
        query = '''
            INSERT INTO artists 
                (first_name, second_name, surname, artist_id, link, extraction_date)
            VALUES
                (%s, %s, %s, %s, %s, %s)
        '''

        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnector.connection.commit()
