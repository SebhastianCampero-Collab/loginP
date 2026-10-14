import pytest
from backend.app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield db
            db.session.remove()
            db.drop_all()

def test_registration(client):
    response = client.post('/register', data={'username': 'testuser', 'password': 'password123'})
    assert response.status_code == 302
    user = User.query.filter_by(username='testuser').first()
    assert user is not None

def test_login_success(client):
    client.post('/register', data={'username': 'testuser2', 'password': 'password123'})
    response = client.post('/login', data={'username': 'testuser2', 'password': 'password123'})
    assert response.status_code == 302

def test_login_failure(client):
    response = client.post('/login', data={'username': 'nonexistent', 'password': 'password'})
    assert response.status_code == 200

def test_logout(client):
    with client.session_transaction() as sess:
        sess['_user_id'] = '1'
    response = client.get('/logout')
    assert response.status_code == 302