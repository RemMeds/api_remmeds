from flask_restplus import Resource, Namespace

from api_remmeds.api.services.compartment_service import add_empty_compartment_new_account

ns = Namespace('compartment', description="Action on user's compartments")


@ns.route('/add_empty_comp/<mail>', methods=['POST'])
class EmptyCompController(Resource):
    @staticmethod
    def post(mail):
        return add_empty_compartment_new_account(mail)

# @ns.route(
#     '/add_empty_comp/<mail>&<com_name>&<com_note>&<com_durationnumb>&<com_durationtext>&<com_check_bf>&<com_check_lun>&<com_check_din>&<com_check_bed>&<com_check_perso_hour>&<com_hour>&<com_frequency>&<com_mon>&<com_tue>&<com_wed>&<com_thu>&<com_fri>&<com_sat>&<com_sun>',
#     methods=['POST'])
# class ConnectionController(Resource):
#     @staticmethod
#     def post(mail, com_name, com_note, com_durationnumb, com_durationtext,
#              com_check_bf, com_check_lun, com_check_din, com_check_bed, com_check_perso_hour,
#              com_hour, com_frequency, com_mon, com_tue, com_wed, com_thu, com_fri, com_sat,
#              com_sun):
#         try:
#             add_empty_compartment_new_account(mail, com_name, com_note, com_durationnumb, com_durationtext,
#                                               com_check_bf, com_check_lun, com_check_din, com_check_bed,
#                                               com_check_perso_hour, com_hour, com_frequency, com_mon, com_tue,
#                                               com_wed, com_thu, com_fri, com_sat, com_sun)
#         except Exception as e:
#             print(e)
