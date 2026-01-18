import requests
from myapp.config import OPENWEATHER_API_KEY
from myapp.models.base import WeatherResponse

def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&lang=zh_cn&units=metric"
    response = requests.get(url)
    data = response.json()
    weather = WeatherResponse(
        temperature=data["main"]["temp"],
        description=data["weather"][0]["description"]
    )
    return f"{city} 当前天气：{weather.description}，气温 {weather.temperature}°C"
