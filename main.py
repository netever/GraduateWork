import web
import purse_ksu
import identify
import save_data
import send_in

html = web.get("https://ksu.edu.ru/travel")
alldata = purse_ksu.get_data(html)
for data in alldata:
        identify.getType(data)
        save_data.save_db(data)
send_in.all()

#https://ksu.edu.ru/travel