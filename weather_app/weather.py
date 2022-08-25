"""
Это главный файл приложения `Погоды`.
"""
from gps_coordinates import get_gps_coordinates
from weather_api_service import get_weather
from base import format_weather
from exceptions import ApiServiceError, CantGetCoordinates


def main():
	try:
		coordinates = get_gps_coordinates()
	except CantGetCoordinates:
		print("Не получил GPS координаты")
		exit(1)
	try:
		weather = get_weather(coordinates)
	except ApiServiceError:
		print(
			"Не смог получить API запрос, ошибка сервера OpenWeather."
			f"По таким координатам: {coordinates}")
		exit(1)
	print(format_weather(weather))


if __name__ == "__main__":
	main()

"""
Kazan, температура 31°C, Ясно
Восход: 05:20
Закат: 19:43
"""