import httpx


class TestClient:
    form_headers = {
        'content-type': 'multipart/form-data; boundary="abcdefg"'
    }

    def get(self, endpoint: str) -> httpx.Response:
        url = self.BASE + endpoint
        return httpx.get(url)

    def put_form(self, endpoint: str, files, **data) -> httpx.Response:
        url = self.BASE + endpoint
        return httpx.put(url, data=data, headers=self.form_headers, files=files)

    def post_form(self, endpoint: str, files, **data) -> httpx.Response:
        url = self.BASE + endpoint
        return httpx.post(url, data=data, headers=self.form_headers, files=files)

    def delete(self, endpoint: str) -> httpx.Response:
        url = self.BASE + endpoint
        return httpx.delete(url)

    @property
    def BASE(self):
        return 'http://localhost:7000'
