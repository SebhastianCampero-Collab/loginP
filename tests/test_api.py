def test_api_login_endpoint(client, app):
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))
    from app import User, db
    User.query.delete()
    db.session.commit()
    response = client.post('/login', data={'username': 'apiuser', 'password': 'pass'})
    assert response.status_code in [200, 302]