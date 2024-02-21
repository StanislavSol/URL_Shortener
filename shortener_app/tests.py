from fastapi.testclient import TestClient
from shortener_app.main import app


client = TestClient(app)


def test_get():
    response = client.get("/")
    print(response.json())
    assert response.status_code == 200

def test_post():
    response = client.post("/")
    assert response.status_code == 200
