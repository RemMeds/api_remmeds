import pymysql


def get_user_contacts(user_id):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute("SELECT * FROM rm_repertory WHERE us_id = '" + user_id + "'")
    contact_list = []
    for req in cur.fetchall():
        contact = {
            "lastname": req[2],
            "firstname": req[3],
            "phonenumber": req[4],
            "mail": req[5],
            "chx_sms": req[6],
            "chx_mail": req[7],
            "note": req[8]
        }
        contact_list.append(contact)
    db.close()
    return contact_list


def add_contact(user_id, my_lastname, my_firstname, my_phone, my_mail, my_chxSMS, my_chxMail, my_note):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute(
        "INSERT INTO rm_repertory (us_id, re_lastname, re_firstname, re_phonenumber, re_mail, "
        "re_chxSMS, re_chxMail, re_note) VALUES ('" + user_id + "', '" + my_lastname + "', '" +
        my_firstname + "', '" + my_phone + "', '" + my_mail + "', '" + my_chxSMS + "', '" +
        my_chxMail + "', '" + my_note + "')")
    db.commit()
    db.close()
