from flask_restplus import Resource, Namespace
from api_remmeds.api.services.repertory_service import get_user_repertory

ns = Namespace('repertory', description='Action on User repertory')


@ns.route('/list_repertory/<user>')
class ListRepertoryController(Resource):
    @staticmethod
    def get(user):
        result = get_user_repertory(user)
        return {"repertory_contact": result}
