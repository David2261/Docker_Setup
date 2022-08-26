import pytest

from exceptions import CantGetCoordinates
from gps_coordinates import get_gps_coordinates




def test_get_gps_coordinates():
	assert get_gps_coordinates()


