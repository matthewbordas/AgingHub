from flask import Flask

#from aginghub.repository import Repository

def test_index_returns_correct_string(test_client: Flask) -> None:
    #res = test_client.get('/api/').data.decode()
    #repo = Repository()
    #assert res.json == repo.get_aging_counter()
    res = test_client.get('/').data.decode()
    assert res == 'Welcome to AgingHub. Check back soon for more!'
    
