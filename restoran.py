import requests, json

location = input("Эта строка указывает географическую область, которая будет использоваться при поиске компаний: ")
latitude = input("Укажіть широту: ")
longitude = input("Укажіть довготу: ")
info_business = []

url = f"https://api.yelp.com/v3/businesses/search?location={location}&latitude={latitude}&longitude={longitude}&sort_by=best_match"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer yGHUwfxURbELVUAES2eWK9wK5oS1eUUlIT80-WStwx2KAGSJ4NyIGn-cC9NsHv8qO3ffm_pCyP3PqIV4pMoruUd2nhZ0SkL3PYNrE0aXyq-iJOxTZxBBhbVdIvEOZHYx"
}

response = requests.get(url, headers=headers)
info_business.append(json.loads(response.text)['businesses'][0]['name'])
info_business.append(json.loads(response.text)['businesses'][0]['image_url'])
info_business.append(json.loads(response.text)['businesses'][0]['coordinates'])
info_business.append(json.loads(response.text)['businesses'][0]['location'])
print(info_business)