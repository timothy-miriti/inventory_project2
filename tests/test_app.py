import pytest
from unittest.mock import patch
from app import app
from inventory import inventory

# Setup 
# This runs before every single test
# It gives each test a fresh fake browser to talk to Flask
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# GET all 
def test_get_all(client):
    res = client.get('/inventory')
    assert res.status_code == 200        # did we get an OK response?
    assert isinstance(res.get_json(), list)  # is the data a list?


# GET one 
def test_get_one_found(client):
    res = client.get('/inventory/1')
    assert res.status_code == 200
    assert res.get_json()['id'] == 1     # is the right item returned?

def test_get_one_not_found(client):
    res = client.get('/inventory/9999')
    assert res.status_code == 404        # does a missing id return 404?


# POST 
def test_add_item(client):
    payload = {
        'product_name': 'Test Juice',
        'brands': 'TestCo',
        'price': 1.50,
        'stock': 10
    }
    res = client.post('/inventory', json=payload)
    assert res.status_code == 201                          # 201 = created
    assert res.get_json()['product_name'] == 'Test Juice' # was it saved?

def test_add_item_missing_name(client):
    res = client.post('/inventory', json={'brands': 'TestCo'})
    assert res.status_code == 400        # missing product_name = bad request?


#  PATCH 
def test_update_item(client):
    res = client.patch('/inventory/1', json={'price': 9.99, 'stock': 100})
    assert res.status_code == 200
    assert res.get_json()['price'] == 9.99   # was price updated?
    assert res.get_json()['stock'] == 100    # was stock updated?

def test_update_item_not_found(client):
    res = client.patch('/inventory/9999', json={'price': 1.00})
    assert res.status_code == 404


# DELETE
def test_delete_item(client):
    res = client.delete('/inventory/2')
    assert res.status_code == 200
    assert 'deleted' in res.get_json()['message']  # is the message correct?

def test_delete_item_not_found(client):
    res = client.delete('/inventory/9999')
    assert res.status_code == 404


# External API (mocked) 
# We don't want to hit the real internet during tests
# So we replace requests.get with a fake that returns fake data
def test_fetch_from_external_api(client):
    mock_response = {
        'status': 1,
        'product': {
            'product_name': 'Mocked Oat Milk',
            'brands': 'MockBrand',
            'ingredients_text': 'Oats, water, salt'
        }
    }
    with patch('external_api.requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_response
        res = client.get('/inventory/fetch/1234567890')
        assert res.status_code == 201
        assert res.get_json()['product_name'] == 'Mocked Oat Milk'

def test_fetch_external_api_not_found(client):
    mock_response = {'status': 0}
    with patch('external_api.requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_response
        res = client.get('/inventory/fetch/0000000000')
        assert res.status_code == 404