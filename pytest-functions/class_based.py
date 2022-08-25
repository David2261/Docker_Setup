from datetime import datetime
from dataclasses import dataclass
from typing import Iterable, Sequence, Mapping


@dataclass
class User:
	birthday: datetime


users = [
	User(birthday=datetime.fromisoformat("2003-08-31")),
	User(birthday=datetime.fromisoformat("2002-07-30")),
	User(birthday=datetime.fromisoformat("2001-06-29"))
]

# Для итерации всех типов хранилищ
def get_younger_user(users: Iterable[User]) -> User:
	if not users: raise ValueError("Пустой User!")
	sorded_users = sorted(users, key=lambda x: x.birthday)
	return sorded_users[0]


def get_user_by_id(user: Sequence[User]) -> User:
	if not users: raise ValueError("Пустой User!")
	print(users[0])
	sorded_users = sorted(users, key=lambda x: x.birthday)
	return sorded_users[0]


def get_user_id(some_users: Mapping[str, User]) -> None:
	print(some_users["bulat"])

get_user_id({
	"bulat": User(birthday=datetime.fromisoformat("2003-08-31")),
	"alex": User(birthday=datetime.fromisoformat("2002-07-30"))
})


class Users:
	def __init__(self, users: Sequence[User]):
		self._users = users

	# Получение объекта по id
	def __getitem__(self, key: int) -> User:
		return self._users[key]

users = Users((
	User(birthday=datetime.fromisoformat("2003-08-31")),
	User(birthday=datetime.fromisoformat("2002-07-30")),
	User(birthday=datetime.fromisoformat("2001-06-29"))
))

def main_get_user_id():
	for u in users:
		print(u)




