from eat_it.app import app

def test_app_has_ping_endpoint():
    with app.test_client() as client:
        response = client.get('/ping')
        assert response.status_code == 501

def test_app_has_users_endpoint_get():
    with app.test_client() as client:
        response = client.get('/users')
        assert response.status_code == 501

def test_app_has_users_endpoint_patch():
    with app.test_client() as client:
        response = client.patch('/users/1')
        assert response.status_code == 501

def test_app_has_users_endpoint_post():
    with app.test_client() as client:
        response = client.post('/users')
        assert response.status_code == 501

def test_app_has_users_endpoint_delete():
    with app.test_client() as client:
        response = client.delete('/users/1')
        assert response.status_code == 501

def test_app_has_user_endpoint_post():
    with app.test_client() as client:
        response = client.post('/users')
        assert response.status_code == 501
    
def test_app_has_user_endpoint_put():
    with app.test_client() as client:
        response = client.put('/users/1')
        assert response.status_code == 501