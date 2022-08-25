from datetime import datetime
from typing import Literal, NamedTuple
from enum import Enum
from geopy.geocoders import Nominatim
import json
from json.decoder import JSONDecodeError
import ssl
import urllib.request
from urllib.error import URLError

from gps_coordinates import Coordinates
from exceptions import ApiServiceError
import config


# Явное лучше не явного.
Celsius = float


class WeatherType(Enum):
	THUNDERSTORM = "Гроза"
	DRIZZLE = "Изморозь"
	RAIN = "Дождь"
	SNOW = "Снег"
	CLEAR = "Ясно"
	FOG = "Туман"
	CLOUDS = "Облачно"


class Weather(NamedTuple):
	temperature: Celsius
	weather_type: WeatherType
	sunrise: datetime
	sunset: datetime
	city: str


# Функция создание запроса по ссылке в config 
def _get_openweather_response(latitude: float, longitude: float) -> str:
	ssl._create_default_https_context = ssl._create_unverified_context
	url = config.OPENWEATHER_URL.format(
		latitude=latitude, longitude=longitude)
	try:
		return urllib.request.urlopen(url).read()
	except URLError:
		raise ApiServiceError

# Функция разбора json запроса
def _parse_openweather_response(openweather_response: str) -> Weather:
	try:
		openweather_dict = json.loads(openweather_response)
	except JSONDecodeError:
		raise ApiServiceError
	return Weather(
		temperature = _parse_temperature(openweather_dict),
		weather_type = _parse_weather_type(openweather_dict),
		sunrise = _parse_sun_time(openweather_dict, "sunrise"),
		sunset = _parse_sun_time(openweather_dict, "sunset"),
		city = "Kazan"
	)


# Функция парсинга температуры
def _parse_temperature(openweather_dict: dict) -> Celsius:
	return round(openweather_dict["main"]["temp"])


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
	try:
		weather_type_id = str(openweather_dict["weather"][0]["id"])
	except (IndexError, KeyError):
		raise ApiServiceError
	weather_types = {
		"1": WeatherType.THUNDERSTORM,
		"3": WeatherType.DRIZZLE,
		"5": WeatherType.RAIN,
		"6": WeatherType.SNOW,
		"7": WeatherType.FOG,
		"800": WeatherType.CLEAR,
		"80": WeatherType.CLOUDS
	}
	for _id, _weather_type in weather_types.items():
		if weather_type_id.startswith(_id):
			return _weather_type
	raise ApiServiceError


# Функция парсинга восхода / заката
def _parse_sun_time(
		openweather_dict: dict,
		time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
	return datetime.fromtimestamp(openweather_dict["sys"][time])


# Функция получения погоды из OpenWeather
def get_weather(coordinates: Coordinates) -> Weather:
	openweather_response = _get_openweather_response(
		longitude=coordinates.longitude, latitude=coordinates.latitude)
	weather = _parse_openweather_response(openweather_response)
	return weather


if __name__ == "__main__":
	print(get_weather(Coordinates(latitude=55.7, longitude=37.6)))

# Пример:
"""
Weather(temperature=31, weather_type=<WeatherType.CLEAR: 'Ясно'>,
sunrise=datetime.datetime(2022, 8, 25, 5, 20, 40),
sunset=datetime.datetime(2022, 8, 25, 19, 43, 18), city='Kazan')
"""
