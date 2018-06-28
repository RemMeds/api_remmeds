from flask_restplus import Resource, Namespace
from api_remmeds.api.services.historic_service import list_historic

ns = Namespace('historic', description='Check the user historic')


@ns.route('/list_historic/<user>')
class HistoricController(Resource):
    @staticmethod
    def get(user):
        result = list_historic(user)
        return {"historic": result}
