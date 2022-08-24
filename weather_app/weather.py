"""
Это главный файл приложения `Погоды`.
"""
from gps_coordinates import get_gps_coordinates
from weather_api_service import get_weather
from base import format_base


def main():
	coordinates = get_gps_coordinates()
	weather = get_weather(coordinates)
	print(format_base(weather))


if __name__ = "__main__":
	main()

