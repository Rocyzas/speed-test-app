import pytest
from flask import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_difficulty(client):
    response = client.get('/api/difficulty/easy')
    assert response.status_code == 200

def test_get_difficulty_invalid(client):
    response = client.get('/api/difficulty/easys')
    assert response.status_code == 400

def test_get_user_input(client):
    data = {'input': 'sample input'}
    response = client.post('/api/userInput', json=data)
    assert response.status_code == 200

def test_get_home(client):
    response = client.get('/')
    assert response.status_code == 200
