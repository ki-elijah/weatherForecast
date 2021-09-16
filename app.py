import requests, json




api_key = "eab568a3c8c70faba0d92c3277f3339b"

base_url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}"

city_name = input("Enter city name: ")
complete_url = base_url + "524901" + api_key + city_name
response = requests.get(complete_url)
x = response.json()
if x["cod"] != "404":
    y = x['main']
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["weather_description"]
    print("Temperature (in Kelvin) = " + str(current_temperature) + 
          "\n atmospheric pressure (in hPa) = " + str(current_pressure) + 
          "\n humidity (in percentage) = " + str(current_humidity) + 
          "\n description = " + str(weather_description))
else:
    print("City not found")
