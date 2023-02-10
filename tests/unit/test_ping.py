from eat_it.app import ping

UNIMPLEMENTED = 501


def test_ping_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED

def test_get_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED

def test_post_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED

def test_put_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED

def test_patch_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED

def test_delete_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED
