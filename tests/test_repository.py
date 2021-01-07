from aginghub.repository import Repository

def test_get_aging_counter_path_succeeds() -> None:
    repo = Repository()
    path = repo.get_aging_counter_path()
    path = path.rsplit('AgingHub', maxsplit=1)
    assert path[1] == '/data/aging_counter.json'

def test_load_aging_counter_is_initially_none() -> None:
    repo = Repository()
    assert repo.get_aging_counter() is None

def test_load_aging_counter_succeeds() -> None:
    repo = Repository()
    repo.load_aging_counter(repo.get_aging_counter_path())
    aging_counter = repo.get_aging_counter()
    assert aging_counter is not None
    assert 'aging' in aging_counter
    assert 'non_aging' in aging_counter
    assert len(aging_counter['aging']) > 0
    assert len(aging_counter['non_aging']) > 0

def test_clear_aging_counter_succeeds() -> None:
    repo = Repository()
    repo.load_aging_counter(repo.get_aging_counter_path())
    repo.clear_aging_counter()
    aging_counter = repo.get_aging_counter()
    assert aging_counter is None