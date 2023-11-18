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

# TO GET THE LINK TO PASTE IN THE BROWSER
print(f"{api}?lat={MY_LAT}&lng={MY_LNG}")

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now)

#separate date and hour
print(sunrise.split("T"))
# se quiser separar as horas basta usar os : como divisor
print(sunrise.split("T")[1].split(":"))
# para mostrar a hora basta entender como lista, o primeiro campo eh o [0]
print(sunrise.split("T")[1].split(":")[0])
