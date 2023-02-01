import sys, os
from datetime import datetime
import pytest

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

from base import format_weather
from weather_api_service import Weather, WeatherType



@pytest.mark.parametrize("temperature, w_type, sunrise, sunset, city",
			[
				(
					25,
					WeatherType.CLEAR,
					datetime.fromisoformat("2022-08-25 05:20:40"),
					datetime.fromisoformat("2022-08-25 19:43:18"),
					'Kazan',
				)
			])


def test_format_weather(temperature, w_type, sunrise, sunset, city):
	assert format_weather(Weather(
			temperature,
			w_type,
			sunrise,
			sunset,
			city))
