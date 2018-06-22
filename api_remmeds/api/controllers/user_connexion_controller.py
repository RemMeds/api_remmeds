from flask_restplus import Resource
from api_remmeds.api.restplus import api
from api_remmeds.api.services.user_connexion_service import check_user_connexion

ns = api.namespace('user_connexion', description='Check if username exist & match with password entered')


@ns.route('/')
class UserController(Resource):
    @staticmethod
    def get():
        return check_user_connexion()
