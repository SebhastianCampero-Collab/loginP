def test_duplicate_registration(client, app):
    with app.app_context():
        from backend.app import User
        User.query.delete()
        db.session.commit()
    response = client.post('/register', data={'username': 'dup', 'password': 'pass1'})
    assert response.status_code == 302
    response = client.post('/register', data={'username': 'dup', 'password': 'pass2'})
    assert 'Usuario ya existe' in str(response.data)