"""
Рассчитать угол между часовой и минутной стрелкой в заданное время  
"""
from datetime import datetime




def time_cacult(time: datetime.time) -> float:
	hour = time.hour
	if hour > 12:
		hour -= 12
	hour_total = 0.5 * (hour * 60 + time.minute)
	minute_total = 6 * time.minute
	total = abs(hour_total - minute_total)
	return min(total, 360 - total)


if __name__ == "__main__":
	print(time_cacult(datetime.now()))

