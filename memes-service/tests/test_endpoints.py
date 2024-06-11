from fastapi.testclient import TestClient
from httpx import Response


class RESPONSE_STATUS:
    OK = 'ok'
    ERROR = 'error'


class STATUS_CODE:
    OK = 200


class TestEndpoints:
    client: TestClient

    @classmethod
    def setup_class(cls):
        from memes_service.app import app
        cls.client = TestClient(app)
        assert cls.client is not None

    def test_get_memes(self):
        response = self.client.get('/memes')
        assert response.status_code == STATUS_CODE.OK
        json_resp = self.get_json(response)

        assert self.is_ok_status(json_resp)
        assert self.has_key(json_resp, 'memes')
        assert self.each_has_key(json_resp['memes'], 'content')
        assert self.each_has_key(json_resp['memes'], 'img_url')

    def each_has_key(self, col: list[dict], key: str) -> bool:
        return all(key in obj for obj in col)

    def is_ok_status(self, obj: dict) -> bool:
        return obj['status'] == RESPONSE_STATUS.OK

    def has_key(self, obj: dict, key: str) -> bool:
        return key in obj

    def is_dict(self, obj) -> bool:
        return isinstance(obj, dict)

    def get_json(self, response: Response) -> dict:
        resp_json = response.json()
        assert self.is_dict(resp_json)
        return response.json()
