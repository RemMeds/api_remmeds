from flask_restplus import Resource, Namespace

from api_remmeds.api.services.contact_service import get_user_contacts
from api_remmeds.api.services.raspberry_service import get_user
from api_remmeds.api.services.historic_service import list_historic, add_historic

ns = Namespace('raspberry', description='Path needed for raspberry synchronization')


@ns.route('/get_user/<user>')
class GetUserController(Resource):
    @staticmethod
    def get(user):
        result = get_user(user)
        return {"user": result}


@ns.route('/list_historic/<user>')
class GetHistoricController(Resource):
    @staticmethod
    def get(user):
        result = list_historic(user)
        return {"historic": result}


@ns.route('/list_contact/<user>')
class ListContactController(Resource):
    @staticmethod
    def get(user):
        result = get_user_contacts(user)
        return {"contact": result}


@ns.route('/add_historic/<user>&<drog_name>&<hour>&<day>&<intake_respected>')
class AddHistoricController(Resource):
    @staticmethod
    def post(user, drog_name, hour, day, intake_respected):
        add_historic(user, drog_name, hour, day, intake_respected)
        return {"creation": "DONE"}
