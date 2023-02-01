import sys, os
import pytest

fpath = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(fpath)

from history import HistoryRecord, WeatherStorage


@pytest.mark.get_type
def test_get_history_type():
	struct = HistoryRecord(date="2022-08-25 05:20:40", weather="Good")
	assert struct


@pytest.mark.get_file
def test_get_file():
	# Проблема: неполучается прописать путь до файла!!!
	file_path = fpath + "/../history.json"
	assert os.path.exists(file_path) == True


