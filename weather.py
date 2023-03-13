import requests, json

all_info_city = []
city = (str(input("City: ")))
api_key = '17e5e96ced879e47af884821a64775e3'
weather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
all_info_city.append(json.loads(weather.text)['name'])
all_info_city.append(json.loads(weather.text)['weather'][0]['main'])
all_info_city.append(json.loads(weather.text)['main']['temp'])
all_info_city.append(json.loads(weather.text)['main']['temp_min'])
all_info_city.append(json.loads(weather.text)['main']['temp_max'])
print(all_info_city)
