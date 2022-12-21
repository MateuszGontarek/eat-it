from eat_it.app import ping, users, user, create_user, delete_user, update_user

def test_ping_returns_501_response():
    result = ping()
    assert result.status_code == 501

def test_users_returns_501_response_get():
    result = users()
    assert result.status_code == 501

def test_user_returns_501_response_patch():
    result = user(1)
    assert result.status_code == 501

def test_create_user_returns_501_response_post():
    result = create_user()
    assert result.status_code == 501

def test_delete_user_returns_501_response_delete():
    result = delete_user(1)
    assert result.status_code == 501

def test_update_user_returns_501_response_put():
    result = update_user(1)
    assert result.status_code == 501



