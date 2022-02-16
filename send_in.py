import telebot
import vk_api
import pymysql
import save_data
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib

def all ():
    if save_data.checkparam('telegram'):
        __telegram()
    if save_data.checkparam('VK'):
        __VK()
    if save_data.checkparam('mail'):
        __mail()


def __telegram ():
    file = open("C://auth.txt", "r")
    token = file.readline()                                             #Берётся токен из файла auth.txt
    token = token[:-1]
    bot = telebot.TeleBot(token)
    bot.config['api_key'] = token
    messages = save_data.news('telegram')                                         #Достаётся новость из базы данных
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
    messages = save_data.news('VK')
    for message in messages:
        strmess = message[1] + '\n' + message[2] + '\n' + message[3]
        vk.wall.post(from_group=1, owner_id='owner_id', message=strmess) #Отправка новости
        time.sleep(2)






def __mail():
    messages = save_data.news('mail')
    for message in messages:
        host = "smtp.gmail.com"
        password = 'password'
        subject = message[1]
        to_addr = []
        if message[5] == 'teacher' or message[5] == 'anybody':
            for user in save_data.news('users'):
                if user[2] == 'teacher' or user[2] == 'anybody':
                    to_addr.append(user[1])
        elif message[5] == 'student' or message[5] == 'anybody':
            for user in save_data.news('users'):
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
