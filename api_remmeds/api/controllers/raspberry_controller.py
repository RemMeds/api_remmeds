from flask_restplus import Resource, Namespace
from api_remmeds.api.services.raspberry_service import get_user

ns = Namespace('raspberry', description='Path needed for raspberry synchronization')


@ns.route('/get_user/<user>')
class ListContactController(Resource):
    @staticmethod
    def get(user):
        result = get_user(user)
        return {"user": result}
