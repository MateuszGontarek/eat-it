from eat_it.views import UserView                            
from flask.views import MethodView
from flask import Response
import pytest

@pytest.fixture
def view() -> UserView:
    return UserView()

def test_user_view_returns_501_on_get_method(view: UserView) -> None:
    actual = view.get("1")
    assert actual.status_code == 501

def test_user_view_returns_response_on_get_method(view: UserView) -> None:
    actual = view.get("1")
    assert isinstance(actual, Response)

def test_user_view_is_subclass_method_view(view: UserView) -> None:
    assert isinstance(view, MethodView)

def test_user_view_returns_201_on_post_method(view: UserView) -> None:
    data = {"name": "test user", "email": "test@example.com"}
    actual = view.post(data)
    assert actual.status_code == 201

def test_user_view_returns_json_on_post_method(view: UserView) -> None:
    data = {"name": "test user", "email": "test@example.com"}
    actual = view.post(data)
    assert actual.mimetype == 'application/json'

def test_user_view_returns_200_on_put_method(view: UserView) -> None:
    data = {"name": "test user updated", "email": "test_updated@example.com"}
    actual = view.put("1", data)
    assert actual.status_code == 200

def test_user_view_returns_json_on_put_method(view: UserView) -> None:
    data = {"name": "test user updated", "email": "test_updated@example.com"}
    actual = view.put("1", data)
    assert actual.mimetype == 'application/json'

def test_user_view_returns_200_on_patch_method(view: UserView) -> None:
    data = {"name": "test user updated partially"}
    actual = view.patch("1", data)
    assert actual.status_code == 200

def test_user_view_returns_json_on_patch_method(view: UserView) -> None:
    data = {"name": "test user updated partially"}
    actual = view.patch("1", data)
    assert actual.mimetype == 'application/json'

def test_user_view_returns_204_on_delete_method(view: UserView) -> None:
    actual = view.delete("1")
    assert actual.status_code == 204
