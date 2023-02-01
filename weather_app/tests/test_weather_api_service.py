import sys, os
import pytest
import requests
from datetime import datetime

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

from weather_api_service import get_weather, Weather, WeatherType
from gps_coordinates import Coordinates


def test_get_weather_response():
	response = get_weather(Coordinates(latitude=55.7, longitude=37.6))

	print(get_weather(Coordinates(latitude=55.7, longitude=37.6)))


def test_get_temperature_correct():
	my_weather = Weather(
			temperature=23,
			weather_type=WeatherType.CLEAR,
			sunrise=datetime.fromisoformat("2022-08-25 05:20:40"),
			sunset=datetime.fromisoformat("2022-08-25 05:20:40"),
			city='Kazan'
			)
	assert my_weather



