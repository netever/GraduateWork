import web
import purse_ksu

html = web.get("https://ksu.edu.ru/travel")
alldata = purse_ksu.get_link(html)


#https://ksu.edu.ru/travel