import web
import purse_ksu
import identify
import save_data

html = web.get("https://ksu.edu.ru/travel")
alldata = purse_ksu.get_data(html)
for data in alldata:
        identify.getType(data)
        save_data.save_db(data)


#https://ksu.edu.ru/travel