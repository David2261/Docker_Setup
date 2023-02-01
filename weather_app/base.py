from weather_api_service import Weather

# Функция форматирования (вывода погоды)
def format_weather(weather: Weather) -> str:
	return (
		f"{weather.city}, температура {weather.temperature}°C, "
		f"{weather.weather_type.value}\n"
		f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
		f"Закат: {weather.sunset.strftime('%H:%M')}\n")


if __name__ == "__main__":
	from datetime import datetime
	from weather_api_service import WeatherType
	print(format_weather(Weather(
		temperature=25,
		weather_type=WeatherType.CLEAR,
		sunrise=datetime.fromisoformat("2022-08-25 05:20:40"),
		sunset=datetime.fromisoformat("2022-08-25 19:43:18"),
		city='Kazan'
	)))

# Пример:
"""
Kazan, температура 25°C, Ясно
Восход: 05:20
Закат: 19:43
"""