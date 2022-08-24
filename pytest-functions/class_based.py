import csv
from typing import Lists


GENDER = ["male", "female", None]

# Функция записи в БД
def write_file(data: Lists) -> None:
	path_db = "pytest-functions/user_info.csv"

	with open(path_db, "w") as file:
		writer = csv.writer(file)
		writer.writerow(
			data
		)


class User:
	name: str
	surname: str
	phone: int
	gender: GENDER
