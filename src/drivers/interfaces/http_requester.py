from abc import ABC, abstractmethod


class HttpRequesterInterface(ABC):
    @abstractmethod
    def request_from_page(self) -> dict[int, str]:
        pass
