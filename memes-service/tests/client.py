import json
import httpx


class TestClient:
    def get(self, endpoint: str) -> httpx.Response:
        url = self.BASE + endpoint
        return httpx.get(url)

    def post(self, endpoint: str, **data) -> httpx.Response:
        url = self.BASE + endpoint
        return httpx.post(url, content=json.dumps(data))

    def put(self, endpoint: str, **data) -> httpx.Response:
        url = self.BASE + endpoint
        return httpx.put(url, content=json.dumps(data))

    def delete(self, endpoint: str) -> httpx.Response:
        url = self.BASE + endpoint
        return httpx.delete(url)

    @property
    def BASE(self):
        return 'http://localhost:7000'
