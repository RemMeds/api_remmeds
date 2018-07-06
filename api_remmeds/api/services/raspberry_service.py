import pymysql


def get_user(user_id):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute("SELECT * FROM rm_user WHERE us_id = '" + user_id + "'")
    user_list = []
    for req in cur.fetchall():
        user = {
            "user_id": req[0],
            "lastname": req[1],
            "firstname": req[2],
            "mail": req[3],
            "pref_breakfast": req[5],
            "pref_lunch": req[6],
            "pref_dinner": req[7],
            "pref_bedtime": req[8]
        }
        user_list.append(user)
    db.close()
    return user_list
