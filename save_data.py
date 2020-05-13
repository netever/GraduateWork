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