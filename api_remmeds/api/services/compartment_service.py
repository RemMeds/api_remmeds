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
                    "INSERT INTO rm_compartment (us_id, com_num, com_name, com_note, com_durationnumb, "
                    "com_durationtext, com_check_perso_hour, com_hour, com_frequency, com_days, com_list_pref) "
                    "VALUES('" + user_id + "', '" + str(i) + "', '', '', '0', 'Jours', '0', '', '0', '', '')")
                db.commit()
        except Exception as e:
            return "Failure" + e
        db.close()
        return "Success"
    else:
        return "Wrong mail"


def list_user_compartment(user_id):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute("SELECT * FROM rm_compartment WHERE us_id = '" + user_id + "'")
    compartment_list = []
    for req in cur.fetchall():
        compartment = {
            "compartment_id": req[0],
            "user_id": req[1],
            "compartment_num": req[2],
            "drug_name": req[3],
            "note": req[4],
            "duration_number": req[5],
            "duration_text": req[6],
            "check_perso_hour": req[7],
            "perso_hour": req[8],
            "frequency": req[9],
            "days": req[10],
            "list_pref": req[11]
        }
        compartment_list.append(compartment)
    db.close()
    return compartment_list


def update_compartment(com_id, com_name, com_note, com_durationnumb, com_durationtext, com_check_perso_hour, com_hour,
                       com_frequency, com_days, com_list_pref):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute(
        "UPDATE rm_compartment SET com_name = '" + com_name + "', com_note = '" + com_note + "', "
        "com_durationnumb = '" + com_durationnumb + "', com_durationtext = '" + com_durationtext + "', "
        "com_check_perso_hour = '" + com_check_perso_hour + "', com_hour = '" + com_hour + "', "
        "com_frequency = '" + com_frequency + "', com_days = '" + com_days + "', "
        "com_list_pref = '" + com_list_pref + "' WHERE com_id = '" + com_id + "'")
    db.commit()
    db.close()
    return "Success"
