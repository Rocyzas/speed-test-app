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
    assert response.status_code != 200

def test_get_difficulty_and_user_input(client):
    difficulty = 'easy'
    response = client.get(f'/api/difficulty/{difficulty}')
    assert response.status_code == 200


    data = {'input': 'This is easy Test'}
    response = client.post('/api/userInput', json=data)
    assert response.status_code == 200
    # currently not checking any contents as haven't decided what it should look like

def test_get_home(client):
    response = client.get('/')
    assert response.status_code == 200
