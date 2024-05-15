import requests
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
bot = Bot(token="6776918028:AAEAZlGknXVrsrz_HigHwMAIflUam8pQW4c")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.reply("Welcome to Weather Bot!\n"
                        "To get weather information, type /weather <city>")


@dp.message_handler(commands=['weather'])
async def send_weather(message: Message):
    city = message.get_args()
    if not city:
        await message.reply("Please specify a city.")
        return

    api_key = "137d62f3c460fac41edca5930e84af7c"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        await message.reply("City not found. Please enter a valid city name.")
        return

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    await message.reply(f"Weather in {city.capitalize()}:\n"
                        f"Description: {weather_description}\n"
                        f"Temperature: {temperature}°C\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} m/s")

executor.start_polling(dp)
