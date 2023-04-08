from flask import Flask, Response, request, jsonify

from eat_it.controllers import AddUserController, UserRequest, \
                               DeleteUserController, UpdateUserController, \
                               PutUserController, GetUserController
from eat_it.repositories import UserRepository
from eat_it.views import UserView

app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=200)


@app.post('/users')
def create_user() -> Response:
    user = request.json
    repository = UserRepository()
    controller = AddUserController(repository=repository)
    add_user_request = UserRequest(user=user)
    controller.add(request=add_user_request)
    return Response(status=200)


@app.delete('/users/<user_id>')
def delete_user() -> Response:
    user = request.json
    repository = UserRepository()
    controller = DeleteUserController(repository=repository)
    delete_user_request = UserRequest(user=user)
    controller.delete(request=delete_user_request)
    return Response(status=200)


@app.patch('/users/<user_id>')
def update_user() -> Response:
    user = request.json
    repository = UserRepository()
    controller = UpdateUserController(repository=repository)
    update_user_request = UserRequest(user=user)
    controller.update(request=update_user_request)
    return Response(status=200)


@app.put('/users/<user_id>')
def put_user() -> Response:
    user = request.json
    repository = UserRepository()
    controller = PutUserController(repository=repository)
    put_user_request = UserRequest(user=user)
    controller.replace(request=put_user_request)
    return Response(status=200)


user_view = UserView.as_view("user_view", controller=GetUserController())
app.add_url_rule('/users/<user_id>', view_func=user_view, method='GET')
app.add_url_rule('/users/<user_id>', view_func=user_view, method='PATCH')
app.add_url_rule('/users/<user_id>', view_func=user_view, method='PUT')
app.add_url_rule('/users', view_func=user_view, method='POST')
app.add_url_rule('/users/<user_id>', view_func=user_view, method='DELETE')



