class HtmlCollectorSpy:

    def __init__(self):
        self.collect_essential_information_attributes = {}

    def collect_essential_information(self, html: str) -> list[dict[str, str]]:
        self.collect_essential_information_attributes['html'] = html
        return [{
            "name": 'someName',
            "link": 'https://something.com'
        }]
