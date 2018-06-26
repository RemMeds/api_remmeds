from flask_restplus import Resource, Namespace
from api_remmeds.api.services.user_connexion_service import check_user_connexion

ns = Namespace('user', description='Check if username exist & match with password entered')


@ns.route('/check_account')
class UserController(Resource):
    @staticmethod
    def get():
        return check_user_connexion()
