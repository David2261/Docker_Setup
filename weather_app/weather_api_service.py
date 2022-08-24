from datetime import datetime
from typing import NamedTuple
from enum import Enum
from geopy.geocoders import Nominatim

from .gps_coordinates import Coordinates

# Находит название объекта
# https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={0b53f78bbb749aeaf71d2ba5e7f033de}

# Явное лучше не явного.
Celsius = int


class WeatherType(Enum):
	THUNDERSTORM = "Гроза"
	DRIZZLE = "Изморозь"
	RAIN = "Дождь"
	SNOW = "Снег"
	CLEAR = "Ясно"
	FOG = "Туман"
	CLOUDS = "Облачно"


# def what_should_i_do(weather_type: WeatherType) -> None:
# 	match weather_type:
# 		case WeatherType.THUNDERSTORM | WeatherType.RAIN:
# 			print("Лучше сиди дома")
# 		case WeatherType.CLEAR:
# 			print("Отличная погода")
# 		case _:
# 			print("Ну так, выходить можно")



class Weather(NamedTuple):
	temperature: Celsius
	weather_type: WeatherType
	sunrise: datetime
	sunset: datetime
	city: str


# Функция получения погоды
def get_weather(coordinates: Coordinates) -> Weather:
	# loc = Nominatim(user_agent="GetLoc")
	# getLocCor = loc.reverse(coordinates[0], coordinates[1])
	return Weather(
		temperature=30,
		weather_type=WeatherType.CLEAR,
		sunrise=datetime.fromisoformat("2022-05-04 04:00:00"),
		sunset=datetime.fromisoformat("2022-05-04 20:25:00"),
		city="Kazan"
	)



# print(locname.address)