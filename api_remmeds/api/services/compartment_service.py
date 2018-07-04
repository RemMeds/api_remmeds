import pymysql

from api_remmeds.api.services.user_connexion_service import get_user_id_from_mail
from api_remmeds.api.services.user_connexion_service import check_mail


def add_empty_compartment_new_account(mail):
    if not check_mail(mail)[0]:
        user_id = str(get_user_id_from_mail(mail))
        db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
        cur = db.cursor()
        try:
            for i in range(1, 9):
                cur.execute(
                    "INSERT INTO rm_compartment (us_id, com_num, com_name, com_note, com_durationnumb, com_durationtext, "
                    "com_check_bf, com_check_lun, com_check_din, com_check_bed, com_check_perso_hour, com_hour, "
                    "com_frequency, com_mon, com_tue, com_wed, com_thu, com_fri, com_sat, com_sun) VALUES('" + user_id + "', "
                    "'" + str(i) + "', '', '', '0', 'Jours', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', "
                    "'0', '0', '0', '0')")
                db.commit()
        except Exception as e:
            return "Failure" + e
        db.close()
        return "Success"
    else:
        return "Wrong mail"
#
#
# def update_compartment(mail, com_name, com_note, com_durationnumb, com_durationtext,
#                        com_check_bf, com_check_lun, com_check_din, com_check_bed, com_check_perso_hour,
#                        com_hour, com_frequency, com_mon, com_tue, com_wed, com_thu, com_fri, com_sat,
#                        com_sun):
#     db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
#     cur = db.cursor()
#     cur.execute(
#         "INSERT INTO rm_compartment (us_id, com_num, com_name, com_note, com_durationnumb, com_durationtext, "
#         "com_check_bf, com_check_lun, com_check_din, com_check_bed, com_check_perso_hour, com_hour, com_frequency, "
#         "com_mon, com_tue, com_wed, com_thu, com_fri, com_sat, com_sun) VALUES('" + user_id + "', "
#         "'" + i + "', '" + com_name + "', '" + com_note + "', '" + com_durationnumb + "', '" + com_durationtext + "', "
#         "'" + com_check_bf + "', '" + com_check_lun + "', '" + com_check_din + "', '" + com_check_bed + "', '" + com_check_perso_hour + "', "
#         "'" + com_hour + "', '" + com_frequency + "', '" + com_mon + "', '" + com_tue + "', '" + com_wed + "', "
#         "'" + com_thu + "', '" + com_fri + "', '" + com_sat + "', '" + com_sun + "')")
#     db.commit()
#     db.close()
#     return "Success"
