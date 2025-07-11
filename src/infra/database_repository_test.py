import pytest
from ..stages.contracts.mocks.transform_contract import transform_contract_mock
from .database_connector import DatabaseConnector
from .database_repository import DatabaseRepository


@pytest.mark.skip(reason='No need to insert data in database')
def test_insert_artist():
    DatabaseConnector.connect()

    database_repo = DatabaseRepository()
    data = transform_contract_mock.load_content[0]

    database_repo.insert_artist(data)
