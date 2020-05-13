import telebot
import vk_api
import pymysql
import time

def all ():
    telegram()
    VK()


def telegram ():
    bot = telebot.TeleBot('token')
    messages = news(False ,True)
    for message in messages:
        strmess = message[1] + '\n' + message[2] + '\n' + message[3]
        if len(strmess) < 4096:
            bot.send_message('@ksu_news', strmess)
        else:
            while len(strmess) > 4096:
                bot.send_message('@ksu_news', strmess[0:4095])
                strmess = strmess[4096:]
                time.sleep(2)
            bot.send_message('@ksu_news', strmess)
        time.sleep(2)


def VK ():
    vk_session = vk_api.VkApi(token='token')
    vk = vk_session.get_api()
    messages = news(True)
    for message in messages:
        strmess = message[1] + '\n' + message[2] + '\n' + message[3]
        vk.wall.post(from_group=1, owner_id='-195203785', message=strmess)
        time.sleep(2)


def news(VK=False, telegram=False):
    connect = pymysql.connect(
        host='localhost',
        port=3308,
        user='root',
        password='',
        db='ksu'
    )
    with connect:
        cursor = connect.cursor()
        if VK == True:
            cursor.execute("SELECT * FROM news WHERE send_vk = 0")
            messages = cursor.fetchall()
            cursor.execute("UPDATE news SET send_vk = 1 WHERE send_vk = 0")
            return messages
        elif telegram == True:
            cursor.execute("SELECT * FROM news WHERE send_telegram = 0")
            messages = cursor.fetchall()
            cursor.execute("UPDATE news SET send_telegram = 1 WHERE send_telegram = 0")
            return messages
