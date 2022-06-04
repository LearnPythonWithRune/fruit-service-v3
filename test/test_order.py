import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.parametrize('test_order', ['banana', 'apple', 'pear'])
def test_post_order(test_order, mocker):
    storage = mocker.patch('app.routers.order.storage')
    response = client.post(
        '/order',
        params={'order': test_order}
    )
    assert storage.ingest.call_count == 1
    assert response.status_code == 200
    assert response.json() == {'Received order': test_order}
