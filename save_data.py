import pymysql


def save_db(data):
    connect = pymysql.connect(
        host='localhost',
        port=1433,
        user='newuser',
        password='Ss145632',
        db='graduatework'
    )

    with connect:
        cursor = connect.cursor()
        sql = "INSERT news (head, text, tags, link, type) VALUES (%s, %s, %s, %s, %s)"
        val = ("" + data['head'], "" + data['text'], "" + data['tags'], "" + data['link'], "" + data['type'])
        cursor.execute(sql, val)