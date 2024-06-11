from fastapi.testclient import TestClient


class RESPONSE_STATUS:
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
        assert response.status_code == RESPONSE_STATUS.OK
        print(response.json())
