from eat_it.app import ping

def test_ping_returns_501_respons():
    result = ping()
    assert result.status_code == 501