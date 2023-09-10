import requests
import json

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=cb4851ff6b0b4fd8b9a52935230909&q={city}"

r = requests.get(url)
print(r.text)
# print(type(r.text))
wdic = json.loads(r.text)
print(wdic["current"]['temp_c'])
