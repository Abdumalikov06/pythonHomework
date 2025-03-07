import requests

api_key='838398eb09be5c4a5220dabdc6f945e0'
city="Tashkent"
URL=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
res=requests.get(URL)
print(res)
if res.status_code ==200:
    data=res.json()
    temp=data["main"]['temp']
    humidity=data['main']['humidity']
    weather=data["weather"][0]['description']
    wind=data['wind']['speed']

    print(f"City= {city}")
    print(f"Temperature: {temp} °C")
    print(f"Humidity: {humidity} %")
    print(f"weather: {weather}")
    print(f"Wind speed: {wind}")
else:
    print("Failed to retrive data. Check you API key")
