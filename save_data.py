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
        sqlres = cursor.execute("SELECT link FROM news WHERE link = '"+data['link']+"'") #поиск такой же новости в бд
        if sqlres == 0:                                                                  #если новости нет в бд
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


def news(setting):
    connect = pymysql.connect(
        host='localhost',
        port=3308,
        user='root',
        password='',
        db='ksu'
    )
    with connect:
        cursor = connect.cursor()
        if setting == 'VK':
            cursor.execute("SELECT * FROM news WHERE send_vk = 0")
            messages = cursor.fetchall()
            cursor.execute("UPDATE news SET send_vk = 1 WHERE send_vk = 0")
            return messages
        elif setting == 'telegram':
            cursor.execute("SELECT * FROM news WHERE send_telegram = 0")
            messages = cursor.fetchall()
            cursor.execute("UPDATE news SET send_telegram = 1 WHERE send_telegram = 0")
            return messages
        elif setting == 'mail':
            cursor.execute("SELECT * FROM news WHERE send_mail = 0")
            messages = cursor.fetchall()
            cursor.execute("UPDATE news SET send_mail = 1 WHERE send_mail = 0")
            return messages
        elif setting == 'users':
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()


def checkparam(setting):
    connect = pymysql.connect(
        host='localhost',
        port=3308,
        user='root',
        password='',
        db='ksu'
    )
    with connect:
        cursor = connect.cursor()
        if setting == 'VK':
            sqlres = cursor.execute("SELECT * FROM `parametres` WHERE id = 1 AND send_vk = TRUE")
            if sqlres > 0:
                return True
        elif setting == 'telegram':
            sqlres = cursor.execute("SELECT * FROM `parametres` WHERE id = 1 AND send_telegram = TRUE")
            if sqlres > 0:
                return True
        elif setting == 'mail':
            sqlres = cursor.execute("SELECT * FROM `parametres` WHERE id = 1 AND send_mail = TRUE")
            if sqlres > 0:
                return True
        return False