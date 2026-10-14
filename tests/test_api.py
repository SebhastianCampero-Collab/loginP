def test_api_login_endpoint(client, app):
    with app.app_context():
        from backend.app import User, db
        User.query.delete()
        db.session.commit()
    response = client.post('/login', data={'username': 'apiuser', 'password': 'pass'})
    assert response.status_code in [200, 302]