import geocoder # type: ignore
from typing import NamedTuple

from exceptions import CantGetCoordinates
from config import *

# NamedTuple почти в 3 раза эффективнее dataclasses
class Coordinates(NamedTuple):
	latitude: float
	longitude: float

# Получение координат
def _get_geocoder_coordinates() -> Coordinates:
	g = geocoder.ip('me')
	if not g:
		CantGetCoordinates()
		exit(1)
	data = g.latlng
	return Coordinates(latitude=data[0], longitude=data[1])


# Функция окрунления
def _round_coordinates(coordinates: Coordinates) -> Coordinates:
	if not USE_ROUNDED_COORDS:
		return coordinates
	return Coordinates(*map(
		lambda c: round(c, 1),
		[coordinates.latitude, coordinates.longitude]
	))


# Мои координаты
def get_gps_coordinates() -> Coordinates:
	coordinates = _get_geocoder_coordinates()
	return _round_coordinates(coordinates)


if __name__ == "__main__":
	print(get_gps_coordinates())

"""
С округлением
Coordinates(latitude=55.8, longitude=37.6)

Без округления
Coordinates(latitude=55.7###, longitude=37.6###)
"""
