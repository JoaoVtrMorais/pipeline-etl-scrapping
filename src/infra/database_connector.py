import os
import psycopg as postgresql
from dotenv import load_dotenv


load_dotenv()


class DatabaseConnector:

    connection = None

    @classmethod
    def connect(cls):
        db_connection = postgresql.connect(

            conninfo=(
                f"host={os.getenv('DB_HOST')} "
                f"port={os.getenv('DB_PORT')} "
                f"dbname={os.getenv('DB_NAME')} "
                f"user={os.getenv('DB_USER')} "
                f"password={os.getenv('DB_PASSWORD')}"
            )
        )
        cls.connection = db_connection
