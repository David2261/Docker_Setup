import sys, os
import pytest
import requests

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

from config import OPENWEATHER_URL


@pytest.mark.run_correct_response
def test_get_request_open_weather():
	response = requests.get(OPENWEATHER_URL.format(
					latitude=55.7, longitude=37.6))
	assert response.status_code == 200


@pytest.mark.run_invalid_response
def test_get_request_open_weather_fail():
	response = requests.get(OPENWEATHER_URL.format(
					latitude=None, longitude=None))
	assert response.status_code == 400

