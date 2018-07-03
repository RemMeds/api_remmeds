import pymysql


def get_user(user_id):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute("SELECT * FROM rm_user WHERE us_id = '" + user_id + "'")
    user_list = []
    for req in cur.fetchall():
        user = {
            "user_id": req[0],
            "lastname": req[2],
            "firstname": req[3],
            "mail": req[4],
            "pref_breakfast": req[6],
            "pref_lunch": req[7],
            "pref_dinner": req[8],
            "pref_bedtime": req[9]
        }
        user_list.append(user)
    db.close()
    return user_list
