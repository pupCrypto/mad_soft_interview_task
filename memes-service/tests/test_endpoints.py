from httpx import Response
from .client import TestClient


class RESPONSE_STATUS:
    OK = 'ok'
    ERROR = 'error'


class STATUS_CODE:
    OK = 200


class TEST_VALUES:
    MEME_ID = 1
    CONTENT = 'Funny Meme'
    NEW_CONTENT = 'New Funny Meme'

    @classmethod
    def GET_TEST_IMG(cls):
        return open('tests/cat.jpg', mode='+rb').read()

    @classmethod
    def GET_NEW_TEST_IMG(cls):
        return open('tests/new-cat.jpeg', mode='+rb').read()


class TestEndpoints:
    client: TestClient

    @classmethod
    def setup_class(cls):
        cls.client = TestClient()
        assert cls.client is not None

    def test_get_memes(self):
        response = self.client.get('/memes')
        assert response.status_code == STATUS_CODE.OK
        json_resp = self.get_json(response)

        assert self.is_ok_status(json_resp)
        assert self.has_key(json_resp, 'memes')
        assert self.each_has_key(json_resp['memes'], 'content')

    def test_get_meme(self):
        response = self.client.get(f'/memes/{TEST_VALUES.MEME_ID}')
        assert response.status_code == STATUS_CODE.OK
        json_resp = self.get_json(response)

        assert self.is_ok_status(json_resp)

        assert self.has_key(json_resp, 'meme_id')
        assert self.is_int(json_resp['meme_id'])

        assert self.has_key(json_resp, 'content')
        assert self.is_str(json_resp['content'])

    def test_create_meme(self):
        files = dict(img=TEST_VALUES.GET_TEST_IMG())
        response = self.client.post_form('/memes', files=files, content=TEST_VALUES.CONTENT)
        assert response.status_code == STATUS_CODE.OK
        json_resp = self.get_json(response)

        assert self.is_ok_status(json_resp)

        assert self.has_key(json_resp, 'meme_id')
        assert self.is_int(json_resp['meme_id'])

    def test_update_meme(self):
        files = dict(img=TEST_VALUES.GET_NEW_TEST_IMG())
        response = self.client.put_form(f'/memes/{TEST_VALUES.MEME_ID}', files=files, content=TEST_VALUES.NEW_CONTENT)
        assert response.status_code == STATUS_CODE.OK
        json_resp = self.get_json(response)

        assert self.is_ok_status(json_resp)

    def test_del_meme(self):
        response = self.client.delete(f'/memes/{TEST_VALUES.MEME_ID}')
        assert response.status_code == STATUS_CODE.OK
        json_resp = self.get_json(response)

        assert self.is_ok_status(json_resp)

    def each_has_key(self, col: list[dict], key: str) -> bool:
        return all(key in obj for obj in col)

    def is_ok_status(self, obj: dict) -> bool:
        return obj['status'] == RESPONSE_STATUS.OK

    def has_key(self, obj: dict, key: str) -> bool:
        return key in obj

    def is_dict(self, obj) -> bool:
        return isinstance(obj, dict)

    def is_int(self, obj) -> bool:
        return isinstance(obj, int)

    def is_str(self, obj) -> bool:
        return isinstance(obj, str)

    def get_json(self, response: Response) -> dict:
        resp_json = response.json()
        assert self.is_dict(resp_json)
        return response.json()
