from datetime import date
from ...drivers.interfaces.http_requester import HttpRequesterInterface
from ...drivers.interfaces.html_collector import HtmlCollectorInterface
from ...stages.contracts.extract_contract import ExtractContract
from ...errors.extract_error import ExtractError


class ExtractHtml:
    def __init__(
        self,
        http_requester: HttpRequesterInterface,
        html_collector: HtmlCollectorInterface,
    ):
        self.__http_requester = http_requester
        self.__html_collector = html_collector

    def extract(self) -> ExtractContract:
        try:
            html_information = self.__http_requester.request_from_page()
            essential_information = self.__html_collector.collect_essential_information(
                html_information["html"]
            )
            return ExtractContract(
                raw_information_content=essential_information,
                extraction_date=date.today()
            )
        except Exception as exception:
            raise ExtractError(str(exception)) from exception
