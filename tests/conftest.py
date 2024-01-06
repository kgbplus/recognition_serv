import pytest
from fastapi.testclient import TestClient
from recognition_serv.app.application import create_application
@pytest.fixture
def test_client():
    app = create_application()
    test_client = TestClient(app)
    return test_client


