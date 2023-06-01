# Third Party Library
from fastapi.testclient import TestClient

# First Party Library
from fastapi_score_server_app.bin.main import app

client = TestClient(app)


def test_read_main() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
