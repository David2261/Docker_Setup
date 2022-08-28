from datetime import datetime
import pytest


from time_total import time_cacult


def test_time_now():
	time_now = datetime.now()
	time_result = time_cacult(time_now)

	hour = time_now.hour
	if hour > 12:
		hour -= 12
	hour_total = 0.5 * (hour * 60 + time_now.minute)
	minute_total = 6 * time_now.minute
	total = abs(hour_total - minute_total)

	my_result = min(total, 360 - total)

	assert time_result == my_result



