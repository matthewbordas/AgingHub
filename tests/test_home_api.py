from aginghub.repository import Repository

def test_home_returns_correct_response(test_client):
    response = test_client.get('/api/home/')
    repo = Repository()
    assert response.json == repo.get_aging_counter()
    
