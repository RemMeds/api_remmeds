from flask import request
from flask_restplus import Resource, Namespace
from api_remmeds.api.services.user_connexion_service import check_user_connexion, check_mail

ns = Namespace('user', description='Check if username exist & match with password entered')


@ns.route('/check_account')
class ConnectionController(Resource):
    @staticmethod
    def get():
        user = request.args['user']
        password = request.args['pass']
        result_connection, user_id = check_user_connexion(user, password)
        return {"connection": result_connection,
                "user_id": user_id}


@ns.route('/check_mail')
class MailController(Resource):
    @staticmethod
    def get():
        mail = request.args['mail']
        result, data = check_mail(mail)
        return {"creation_posibility": result,
                "data": data}
