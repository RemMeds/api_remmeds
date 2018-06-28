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


def update_account(your_mail, your_lastname, your_firstname, your_bf, your_lun, your_din, your_bed):
    db = pymysql.connect(host='localhost', user='root', password='azerty', db='remmeds_users')
    cur = db.cursor()
    cur.execute(
        "UPDATE rm_user SET us_lastname = '" + your_lastname + "', us_firstname = '" + your_firstname +
        "', us_prefbreakfast = '" + your_bf + "', us_preflunch = '" + your_lun + "', us_prefdinner = '" +
        your_din + "', us_prefbedtime = '" + your_bed + "' WHERE us_mail = '" + your_mail + "'")
    db.commit()
    db.close()
