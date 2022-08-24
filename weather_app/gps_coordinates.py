import geocoder
from typing import NamedTuple
from subprocess import Popen, PIPE

from exceptions import CantGetCoordinates

# NamedTuple почти в 3 раза эффективнее dataclasses
class Coordinates(NamedTuple):
	latitude: float
	longitude: float


# Мои координаты
def get_gps_coordinates() -> Coordinates:
	g = geocoder.ip('me')
	data = g.latlng
	return Coordinates(latitude=data[0], longitude=data[1])


if __name__ = "__main__":
	print(get_gps_coordinates())
