import python_weather
import asyncio

async def getweather():
    client = python_weather.Client(format=python_weather.METRIC)

    city = input("Please Enter City: ")
    print('****************************************************************')
    print("+++++" + city + "+++++")
    weather = await client.find(city)

    print("Date: ", weather.current.date)
    print("The current temperature is: ", weather.current.temperature)
    print("The current humidity is: ", weather.current.humidity)
    print("The current wind speed is: ", weather.current._get('@windspeed'))
    print("Feels like: ", weather.current.feels_like)

    for forecast in weather.forecasts:
        print("The temperature on the " + str(forecast.date) + " is/was:",
              forecast.sky_text, forecast.temperature)

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
