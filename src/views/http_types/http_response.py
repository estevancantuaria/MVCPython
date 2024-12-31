from typing import Dict

class HttpResponse:
    def __init__(self, body: Dict = None, status_code: int = 200) -> None:
        self.body = body
        self.status_code = status_code
