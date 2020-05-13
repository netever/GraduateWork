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