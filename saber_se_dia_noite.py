import requests
from datetime import datetime

api = "https://api.sunrise-sunset.org/json"

MY_LAT = 53.799690
MY_LNG = -1.549100

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(api, params=parameters)
response.raise_for_status()
data = response.json()
print(data)



sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
