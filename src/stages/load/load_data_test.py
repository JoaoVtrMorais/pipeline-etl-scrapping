import pytest
from ...stages.contracts.mocks.transform_contract import transform_contract_mock
from .load_data import LoadData
from ...errors.load_error import LoadError

class RepositorySpy:
    def __init__(self):
        self.insert_artist_attributes = []

    def insert_artist(self, data):
        self.insert_artist_attributes.append(data)

def test_load():
    repo = RepositorySpy()
    load_data = LoadData(repo)

    load_data.load(transform_contract_mock)
    assert repo.insert_artist_attributes == transform_contract_mock.load_content


def test_load_error():
    repo = RepositorySpy()
    load_data = LoadData(repo)

    with pytest.raises(LoadError):
        load_data.load('Entrada com Erro')
