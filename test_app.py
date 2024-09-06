import pytest
from app import app, db
from app.models import User, Movie


@pytest.fixture
def client(setup_database):
    app.testing = True
    with app.test_client() as client:
        yield client

def test_add_movie_page(client):
    response = client.get('/add_movie')
    assert response.status_code == 200
    assert b'Add Movie' in response.data
    assert b'<form' in response.data
    assert b'name="user_id"' in response.data
    assert b'name="title"' in response.data

def test_update_movie_page(client):
    response = client.get('/users/1/update_movie/1')
    assert response.status_code == 200
    assert b'Update Movie' in response.data

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to MovieWeb App!' in response.data

def test_404_error(client):
    response = client.get('/non_existent_page')
    assert response.status_code == 404
    assert b'Page Not Found' in response.data

def test_add_movie_empty_form(client):
    response = client.post('/add_movie', data={})
    assert response.status_code == 400

def test_add_movie_invalid_user_id(client):
    response = client.post('/add_movie', data={'user_id': 'abc', 'title': 'Test Movie'})
    assert response.status_code == 400

def test_add_movie_invalid_title_length(client):
    long_title = 'This is a very long title that exceeds the allowed character limit'
    response = client.post('/add_movie', data={'user_id': 1, 'title': long_title})
    assert response.status_code == 400