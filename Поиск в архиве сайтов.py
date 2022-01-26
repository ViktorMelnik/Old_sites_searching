import webbrowser
import requests

print("Давайте найдём старый сайт")
site = input("Введите URL старого сайта: ")
data = input("Введите год, месяц, день, в который, как вы помните, этот сайт ещё работал. Пример: 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, data)
response = requests.get(url)
data = response.json()
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Нашли эту копию: ", old_site)
    print("Теперь он должен появиться в вашем браузере.")
    webbrowser.open(old_site)
except:
    print("Неудалось найти", site)
