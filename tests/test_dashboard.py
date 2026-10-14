def test_logged_in_user_can_access_index(client, app):
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))
    from app import User, db
    user = User.query.first()