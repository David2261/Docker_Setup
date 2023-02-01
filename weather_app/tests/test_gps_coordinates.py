import sys, os
import pytest

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

from exceptions import CantGetCoordinates
from gps_coordinates import get_gps_coordinates, Coordinates




def test_get_gps_coordinates():
	assert get_gps_coordinates() == Coordinates(latitude=55.8, longitude=37.6)


