# tests/test_conexao_repository.py

def test_insert(repository):
    repository.insert("test_collection", name="test_name", value=123)
    result = repository.select("test_collection", name="test_name")
    assert result is not None
    assert result['name'] == "test_name"
    assert result['value'] == 123

def test_insert_despesas(repository):
    repository.insert("test_collection", name="test_name")
    repository.insertDespesas("test_collection", {'name': 'test_name'}, expense=789)
    result = repository.select("test_collection", name="test_name")
    assert result is not None
    assert 'expense' in result and 789 in result['expense']

def test_delete(repository):
    repository.insert("test_collection", name="test_name", value=123)
    repository.delete("test_collection", name="test_name")
    result = repository.select("test_collection", name="test_name")
    assert result is None

def test_execute_aggregation(repository):
    repository.insert("test_collection", name="test_name", value=123)
    filter_kwargs = {'name': 'test_name'}
    update_kwargs = {'$set': {'value': 456}}
    query = filter_kwargs
    update = update_kwargs
    kwargs = [query, update]  # Alteração aqui para passar filter e update como uma lista
    repository.executeAggregation("test_collection", kwargs)
    result = repository.select("test_collection", name="test_name")
    assert result is not None
    assert result['value'] == 456