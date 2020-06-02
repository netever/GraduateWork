import pymysql


def save_db(data):
    connect = pymysql.connect(
        host='localhost',
        port=3308,
        user='root',
        password='',
        db='ksu'
    )


    with connect:
        cursor = connect.cursor()
        sqlres = cursor.execute("SELECT link FROM news WHERE link = '"+data['link']+"'")
        if sqlres == 0:
            sql = "INSERT news (head, text, tags, link, type) VALUES (%s, %s, %s, %s, %s)"
            val = ("" + data['head'], "" + data['text'], "" + data['tags'], "" + data['link'], "" + data['type'])
            cursor.execute(sql, val)

def save_user(email, role):
    connect = pymysql.connect(
        host='localhost',
        port=3308,
        user='root',
        password='',
        db='ksu'
    )

    with connect:
        cursor = connect.cursor()
        sqlres = cursor.execute("SELECT email FROM users WHERE email = '"+email+"'")
        if sqlres == 0:
            sql = "INSERT users (email, role) VALUES (%s, %s)"
            val = ("" + email, "" + role)
            cursor.execute(sql, val)
        elif sqlres > 0:
            cursor.execute("UPDATE users SET role = '" + role + "' WHERE email = '" + email + "'")

def del_user(email):
    connect = pymysql.connect(
        host='localhost',
        port=3308,
        user='root',
        password='',
        db='ksu'
    )

    with connect:
        cursor = connect.cursor()
        sqlres = cursor.execute("SELECT email FROM users WHERE email = '"+email+"'")
        if sqlres > 0:
            sql = "DELETE FROM users WHERE email = '"+email+"'"
            cursor.execute(sql)

def checkuser(user, passw):
    connect = pymysql.connect(
        host='localhost',
        port=3308,
        user='root',
        password='',
        db='ksu'
    )

    with connect:
        cursor = connect.cursor()
        sqlres = cursor.execute("SELECT login FROM admins WHERE password = '" + passw + "' AND login = '"+user+"'")
        if sqlres > 0:
            return True
    return False

def changeparam(vk, telegram, mail):
    connect = pymysql.connect(
        host='localhost',
        port=3308,
        user='root',
        password='',
        db='ksu'
    )

    with connect:
        cursor = connect.cursor()
        if vk == 'true':
            sqlres = cursor.execute("UPDATE parametres SET send_vk = TRUE WHERE id = 1")
        if telegram == 'true':
            sqlres = cursor.execute("UPDATE parametres SET send_telegram = TRUE WHERE id = 1")
        if mail == 'true':
            sqlres = cursor.execute("UPDATE parametres SET send_mail = TRUE WHERE id = 1")
        if vk == 'false':
            sqlres = cursor.execute("UPDATE parametres SET send_vk = FALSE WHERE id = 1")
        if telegram == 'false':
            sqlres = cursor.execute("UPDATE parametres SET send_telegram = FALSE WHERE id = 1")
        if mail == 'false':
            sqlres = cursor.execute("UPDATE parametres SET send_mail = FALSE WHERE id = 1")
    return False