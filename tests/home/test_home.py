from aginghub.repository import Repository

def test_home_returns_index_html(test_client):
    response = test_client.get('/')
    content = response.data.decode()
    assert content.find('AgingHub') != -1
    assert response.status_code == 200

def test_home_api_returns_aging_counter(test_client):
    response = test_client.get('/api/home')
    repo = Repository()
    assert response.json == repo.get_aging_counter()
    
