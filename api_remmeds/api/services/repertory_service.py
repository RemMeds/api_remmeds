import pymysql


def get_user_repertory(user_id):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute("SELECT * FROM rm_repertory WHERE us_id = '" + user_id + "'")
    l = []
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
        l.append(contact)
    db.close()
    return l
