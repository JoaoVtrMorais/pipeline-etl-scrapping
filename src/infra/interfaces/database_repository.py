from abc import ABC, abstractmethod


class DatabaseRepositoryInterface(ABC):

    @classmethod
    @abstractmethod
    def insert_artist(cls, data: dict) -> None:
        pass
