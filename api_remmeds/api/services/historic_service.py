import pymysql


def list_historic(user_id):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute("SELECT * FROM rm_historic WHERE us_id = '" + user_id + "'")
    historic_list = []
    for req in cur.fetchall():
        historic = {
            "medicine_name": req[2],
            "hour": req[3],
            "day": req[4],
            "respected": req[5]
        }
        historic_list.append(historic)
    db.close()
    return historic_list
