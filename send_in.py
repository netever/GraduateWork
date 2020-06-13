import telebot
import vk_api
import pymysql
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib

def all ():
    if __checkparam('telegram'):
        __telegram()
    if __checkparam('VK'):
        __VK()
    if __checkparam('mail'):
        __mail()


def __telegram ():
    file = open("C://auth.txt", "r")
    token = file.readline()                                             #Берётся токен из файла auth.txt
    bot = telebot.TeleBot(token)
    bot.config['api_key'] = token
    messages = __news('telegram')                                         #Достаётся новость из базы данных
    for message in messages:
        strmess = message[1] + '\n' + message[2] + '\n' + message[3]    #Вставляется в сообщение заголовок,
                                                                        #текст и тэги
        if len(strmess) < 4096:                                         #В телеграме стоит ограничение сообщения
            bot.send_message('@ksu_news', strmess)                      #на 4096 символов, поэтому разбиваем
        else:                                                           #новость на несколько частей, если её
            while len(strmess) > 4096:                                  #длина больше 4096 символов
                bot.send_message('@ksu_news', strmess[0:4095])
                strmess = strmess[4096:]
                time.sleep(2)
            bot.send_message('@ksu_news', strmess)                      #отправка сообщения
        time.sleep(2)


def __VK ():
    file = open("C://auth.txt", "r")
    file.readline()
    token = file.readline()                                 #Берётся токен из файла auth.txt
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()                               #Авторизация по api вконтакте
    messages = __news('VK')
    for message in messages:
        strmess = message[1] + '\n' + message[2] + '\n' + message[3]
        vk.wall.post(from_group=1, owner_id='-195203785', message=strmess) #Отправка новости
        time.sleep(2)


def __news(setting):
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

def __checkparam(setting):
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

def __mail():
    messages = __news('mail')
    for message in messages:
        host = "smtp.gmail.com"
        password = 'ss145632'
        subject = message[1]
        to_addr = []
        if message[5] == 'teacher' or message[5] == 'anybody':
            for user in __news('users'):
                if user[2] == 'teacher' or user[2] == 'anybody':
                    to_addr.append(user[1])
        elif message[5] == 'student' or message[5] == 'anybody':
            for user in __news('users'):
                if user[2] == 'student' or user[2] == 'anybody':
                    to_addr.append(user[1])
        from_addr = "kgunovosti@gmail.com"
        body_text = message[2]

        msg = MIMEText('' + body_text, 'plain', 'utf-8')
        msg['Subject'] = Header('' + subject, 'utf-8')
        msg['From'] = from_addr
        msg['To'] = ", ".join(to_addr)

        server = smtplib.SMTP(host, 587)
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        time.sleep(2)