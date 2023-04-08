from flask.views import MethodView
from eat_it.controllers import UserController
from flask import Response



class UserView(MethodView):
    def __init__(self, controller: UserController) -> None:
        self._get_user_controller = controller

    def get(self, id: str) -> Response:
       return Response(status=501)
    
    def delete(self, id: str) -> Response:
        return Response(status=204)
    
    def post(self, data: dict) -> Response:
        return Response(status=201)
    
    def put(self, id: str, data: dict) -> Response:
        return Response(status=200)
    
    def patch(self, id: str, data: dict) -> Response:
        return Response(status=200)
    
    
    
