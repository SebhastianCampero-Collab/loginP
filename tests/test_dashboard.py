def test_logged_in_user_can_access_index(client, app):
    with app.app_context():
        from backend.app import User, db
        user = User.query.first()
        with client.session_transaction() as sess:
            sess['_user_id'] = user.id
    response = client.get('/')
    assert response.status_code == 200