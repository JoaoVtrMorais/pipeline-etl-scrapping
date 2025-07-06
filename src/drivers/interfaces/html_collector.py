from abc import ABC, abstractmethod


class HtmlCollectorInterface(ABC):

    @classmethod
    @abstractmethod
    def collect_essential_information(cls, html: str) -> list[dict[str, str]]:
        pass
