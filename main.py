import web
import purse_ksu
import identify
import save_data
import send_in

html = web.get("https://ksu.edu.ru/travel")     #скачиваются новости
alldata = purse_ksu.get_data(html)              #новости разбиваются на части,
                                                #где уже отдельны ссылки на новости,
                                                #заголовки и т.д.
for data in alldata:
        identify.getType(data)                  #определяется для кого новость
        save_data.save_db(data)                 #новость сохраняется в базу данных
send_in.all()                                   #рассылка новостей