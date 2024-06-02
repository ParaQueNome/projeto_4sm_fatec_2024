import pytest
import mongomock


def test_insert(db):
    db.insert("test_collection", name="test_name", value=123)
    result = db.select("test_collection", name="test_name")
    assert result is not None
    assert result['name'] == "test_name"
    assert result['value'] == 123

def test_insert_despesas(db):
    db.insert("test_collection", name="test_name")
    db.insertDespesas("test_collection", {'name': 'test_name'}, expense=789)
    result = db.select("test_collection", name="test_name")
    assert result is not None
    assert 'expense' in result and 789 in result['expense']

def test_delete(db):
    db.insert("test_collection", name="test_name", value=123)
    db.delete("test_collection", name="test_name")
    result = db.select("test_collection", name="test_name")
    assert result is None

def test_execute_aggregation(db):
    db.insert("test_collection", name="test_name", value=123)
    db.executeAggregation("test_collection", [{'name': 'test_name'}, {'$set': {'value': 456}}])
    result = db.select("test_collection", name="test_name")
    assert result is not None
    assert result['value'] == 456