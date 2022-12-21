from eat_it.app import app

def test_app_has_ping_endpoint():
    with app.test_client() as client:
        response = client.get('/ping')
        assert response.status_code == 501