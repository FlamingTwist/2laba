import requests
import json

city = "Moscow,RU"

appid = "bfe66093d053f44991f03596042e278f"

# отправляем запрос с нужными параметрами
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q':city, 'units':'metric', 'lang':'ru', 'APPID':appid} )


data = res.json()

print(data)

