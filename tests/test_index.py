from flask import Flask

from aginghub.repository import Repository

def test_index_returns_correct_response(test_client: Flask) -> None:
    response = test_client.get('/api/')
    repo = Repository()
    assert response.json == repo.get_aging_counter()
    
