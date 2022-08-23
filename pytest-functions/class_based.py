from typing import Literal
import datetime


class User:
	username: str
	surname: str
	phone: int
	gender: GENDER
	created_at: datetime.datetime


GENDER = Literal("male", "female", "none")

def validate_user(user: User):
	...


def main():
	user_id = 123
	validate_user(user_id)

if __name__ == '__main__':
	main()
