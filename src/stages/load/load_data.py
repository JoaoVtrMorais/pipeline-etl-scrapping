from ...infra.interfaces.database_repository import DatabaseRepositoryInterface
from ...stages.contracts.transform_contract import TransformContract
from ...errors.load_error import LoadError


class LoadData:
    def __init__(self, repository: DatabaseRepositoryInterface):
        self.__repository = repository

    def load(self, transformed_data_contract: TransformContract) -> None:
        try:
            load_content = transformed_data_contract.load_content
            for data in load_content:
                self.__repository.insert_artist(data)
        except Exception as exception:
            raise LoadError(str(exception)) from exception
