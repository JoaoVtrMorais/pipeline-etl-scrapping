class HttpRequesterSpy:
    def __init__(self):
        self.request_from_page_count = 0

    def request_from_page(self) -> dict[int, str]:
        self.request_from_page_count += 1
        return {
            "status_code": 200,
            "html": '<h1>OlaMundo</h1>'
        }
