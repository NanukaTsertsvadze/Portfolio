import requests
import json
import schedule
import win10toast

#Making request 

city = 'Tbilisi'
key = "887aaff89bee4fd742287bfd4afa2483"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
response = requests.get(url)
result = response.json()

#Making new Json file and Writing info In it

file = open("Weather.json", "w")
json_obj = json.loads(response.text)
json_structured = json.dumps(json_obj, indent=4)
file.write(json_structured)
file.close()


#Taking info from Json And Showing on Windows Bar

temp = result["main"]["temp"]
wind = result["wind"]["speed"]

def weather():
    toast = win10toast.ToastNotifier()
    city_name = 'Tbilisi'
    API_key = '887aaff89bee4fd742287bfd4afa2483'
    payload = {'q':city_name, 'appid':API_key, 'units':'metric'}
    url = f'https://api.openweathermap.org/data/2.5/weather'
    resp = requests.get(url, params=payload)
    data = resp.json()
    weather_tbilisi = data['main']['temp']
    toast.show_toast(title='ტემპერატურა თბილისში', msg=f'{weather_tbilisi} გრადუსი', duration=5)

schedule.every(10).seconds.do(weather)
while True:
    schedule.run_pending()