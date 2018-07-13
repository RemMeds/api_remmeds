from flask_restplus import Resource, Namespace
from api_remmeds.api.services.historic_service import list_historic, add_historic

ns = Namespace('historic', description='Check the user historic')


@ns.route('/list_historic/<user>')
class HistoricController(Resource):
    @staticmethod
    def get(user):
        result = list_historic(user)
        return {"historic": result}


@ns.route('/add_historic/<user>&<drug_name>&<hour>&<day>&<intake_respected>&<num_comp>&<time_slot>')
class AddHistoricController(Resource):
    @staticmethod
    def post(user, drug_name, hour, day, intake_respected, num_comp, time_slot):
        add_historic(user, drug_name, hour, day, intake_respected, num_comp, time_slot)
        return {"creation": "DONE"}
