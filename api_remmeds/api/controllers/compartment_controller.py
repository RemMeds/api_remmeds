from flask_restplus import Resource, Namespace

from api_remmeds.api.services.compartment_service import list_user_compartment, update_compartment

ns = Namespace('compartment', description="Action on user's compartments")


@ns.route('/list_com/<user_id>')
class ListCompartmentController(Resource):
    @staticmethod
    def get(user_id):
        response = list_user_compartment(user_id)
        return {"compartment": response}


@ns.route(
    '/update_com/<com_id>&<com_name>&<com_note>&<com_durationnumb>&<com_durationtext>&<com_check_perso_hour>&<com_hour>&<com_frequency>&<com_days>&<com_list_pref>', methods=['POST'])
class UpdateCompartmentController(Resource):
    @staticmethod
    def post(com_id, com_name, com_note, com_durationnumb, com_durationtext, com_check_perso_hour, com_hour,
            com_frequency, com_days, com_list_pref):
        update_compartment(com_id, com_name, com_note, com_durationnumb, com_durationtext, com_check_perso_hour,
                           com_hour,
                           com_frequency, com_days, com_list_pref)
