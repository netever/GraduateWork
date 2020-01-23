import web
import purse_ksu
import identify

html = web.get("https://ksu.edu.ru/travel")
alldata = purse_ksu.get_data(html)
for data in alldata:
    identify.getType(data)


#https://ksu.edu.ru/travel