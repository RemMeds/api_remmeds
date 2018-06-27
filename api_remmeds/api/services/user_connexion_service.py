import pymysql


def check_user_connexion(your_mail, your_password):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute("SELECT us_id FROM rm_user WHERE us_mail = '" + your_mail + "' AND us_mdp = '" + your_password + "'")
    response = cur.fetchall()
    db.close()
    if not response:
        return False, False
    else:
        return True, response[0][0]
