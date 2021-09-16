import python_weather
import asyncio

async def getweather():
    client = python_weather.Client(format=python_weather.IMPERIAL)

    city = input("Please Enter City: ")
    weather = await client.find(city)

    print("The current temperature is: ", weather.current.temperature)
    print("The current humidity is: ", weather.current.humidity)
    #print(weather.current.pressure)

    for forecast in weather.forecasts:
        print("The temperature on the is/was" + str(forecast.date) + " is: ",
              forecast.sky_text, forecast.temperature)

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
