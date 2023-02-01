
# При True - координаты будут округляться
USE_ROUNDED_COORDS = True

OPENWEATHER_API = "0b53f78bbb749aeaf71d2ba5e7f033de"


OPENWEATHER_URL = (
	"https://api.openweathermap.org/data/2.5/weather?"
	"lat={latitude}&lon={longitude}&"
	"appid="+ OPENWEATHER_API + "&lang=ru&units=metric"
)

# lat=33.44&lon=-94.04