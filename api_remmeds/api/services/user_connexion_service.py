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


def check_mail(your_mail):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute("SELECT * FROM rm_user WHERE us_mail = '" + your_mail + "'")
    response = cur.fetchall()
    db.close()
    if not response:
        return True, "Let's create this account"
    else:
        return False, "Already in database, can't create this user"


def create_account(your_mail, your_password):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute("INSERT INTO rm_user (us_mail, us_mdp) VALUES ('" + your_mail + "', '" + your_password + "')")
    db.commit()
    db.close()
