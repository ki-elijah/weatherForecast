import python_weather
import asyncio

async def getweather():
    client = python_weather.Client(format=python_weather.METRIC)

    city = input("Please Enter City: ")
    weather = await client.find(city)

    print("The current temperature is: ", weather.current.temperature)
    print("The current humidity is: ", weather.current.humidity)

    for forecast in weather.forecasts:
        print("The temperature on the " + str(forecast.date) + " is/was:",
              forecast.sky_text, forecast.temperature)

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
