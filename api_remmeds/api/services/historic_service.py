import pymysql


def list_historic(user_id):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute("SELECT * FROM rm_historic WHERE us_id = '" + user_id + "'")
    historic_list = []
    for req in cur.fetchall():
        historic = {
            "drug_name": req[2],
            "hour": req[3],
            "day": req[4],
            "respected": req[5],
            "num_comp": req[6],
            "time_slot": req[7]
        }
        historic_list.append(historic)
    db.close()
    return historic_list


def add_historic(user_id, drug_name, hour, day, intake_respected, num_comp, time_slot):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute(
        "INSERT INTO rm_historic (us_id, hi_drugname, hi_hours, hi_day, hi_takenrespected, hi_num_comp, hi_time_slot) VALUES ('" + user_id + "', '" + drug_name + "', '" + hour + "', '" + day + "', '" + intake_respected + "', '" + num_comp + "', '" + time_slot + "')")
    db.commit()
    db.close()
