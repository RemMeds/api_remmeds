from flask_restplus import Resource, Namespace
from api_remmeds.api.services.historic_service import list_historic, add_historic

ns = Namespace('historic', description='Check the user historic')


@ns.route('/list_historic/<user>')
class HistoricController(Resource):
    @staticmethod
    def get(user):
        result = list_historic(user)
        return {"historic": result}


@ns.route('/add_historic/<user>&<drog_name>&<hour>&<day>&<intake_respected>')
class AddHistoricController(Resource):
    @staticmethod
    def post(user, drog_name, hour, day, intake_respected):
        add_historic(user, drog_name, hour, day, intake_respected)
        return {"creation": "DONE"}
