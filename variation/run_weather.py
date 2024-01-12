# #!!!!! сщздаем конфиг окружения
# import subprocess
#
# # установленные пакеты
# installed_packages = subprocess.check_output(['pip', 'freeze']).decode('utf-8').split('\n')
#
# # список пакетов в файл
# with open('requirements.txt', 'w') as f:
#     for package in installed_packages:
#         f.write(package + '\n')


import requests
import json
import pandas as pd
from datetime import datetime

api_key = '2ea065df301249e1a6b154936240701'

# https://api.weatherapi.com/v1/current.json?key=2ea065df301249e1a6b154936240701&q=Berlin, Belgrade, Novi Sad, Podgorica, Herceg-Novi, Tivat, Limassol, Tel Aviv, Saint Petersburg, Gorno-Altaysk, Tbilisi, Erevan&aqi=no

cities = ['Berlin', 'Belgrade', 'Novi Sad']
url = 'https://api.weatherapi.com/v1/current.json?key=2ea065df301249e1a6b154936240701&aqi=no&q='
finalRes = []

for i in cities:
    response = requests.get(url + i)
    try:
        res = response.json()
        if 'error' in res:
            print(f"Ошибка для {i}: {res['error']['message']}")
        else:
            data = {}
            data['city'] = i
            data['time'] = res['current']['last_updated']
            data['temp_c'] = res['current']['temp_c']
            data['wind_kph'] = res['current']['wind_kph']
            data['cloud'] = res['current']['cloud']
            finalRes.append(data)
    except Exception as e:
        print(f"Ошибка для {i}: {e}")

print(finalRes)

df = pd.DataFrame(finalRes)
df.to_csv('weather.csv', index=False)


# =========================================================
# прогноз
#

 #
 # cities = ['Berlin', 'Belgrade', 'Novi Sad']
 # url = 'http://api.weatherapi.com/v1/forecast.json?key=2ea065df301249e1a6b154936240701&days=3&q='
 # finalRes = []
 #
 # for i in cities:
 # 	res = json.loads(requests.get(url + i).text)
 # 	try:
 # 		for j in res['forecast']['forecastday']:
 # 			for k in j['hour']:
 # 				individual = {}
 # 				individual['city']   = i
 # 				individual['hour']   = k['time']
 # 				individual['temp_c'] = k['temp_c']
 # 				individual['wind_kph'] = k['wind_kph']
 # 				individual['cloud'] = k['cloud']
 #
 # 	except Exception as e:
 # 		print(e)
 # pd.DataFrame(finalRes).to_csv('weather.csv')
 #
 # ==============================================