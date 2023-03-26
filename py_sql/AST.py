"""The area of a spherical tringle"""
import sqlite3
import datetime
import math as m
from itertools import groupby

from config import file


try:
	connection = sqlite3.connect(file, uri=True)
except Exception as ex:
	print("Connection refused...")
	print(ex)

currentDateTime = datetime.datetime.now()


# Площадь сферического треугольника
class AST:
	def __init__(self, A, B, C, R):
		self.A = A
		self.B = B
		self.C = C
		self.R = R

	def area_spherical(self):
		ABC = (self.A + self.B + self.C - m.pi) * pow(self.R, 2)
		return ABC


def main():
	A = 32
	B = 25
	C = 24
	R = 50
	cursor = connection.cursor()
	try:
		create_table_query = """CREATE TABLE IF NOT EXISTS AST (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			A INTEGER,
			B INTEGER,
			C INTEGER,
			R INTEGER,
			AST_Count INTEGER,
			SubmissionDate TIMESTAMP);"""
		cursor.execute(create_table_query)
	except Exception as ex:
		print(f'Create table error...\n{ex}')
	count_query_all = 0
	try:
		count_query = """SELECT COUNT(id)
		FROM AST WHERE id='1'"""
		count_query_all = cursor.execute(count_query)
	except Exception as ex:
		print(f"Error with count query all...\n{ex}")
	try:
		ast = AST(A, B, C, R)
		try:
			insertQuery = """INSERT INTO AST
			VALUES (?, ?, ?, ?, ?, ?, ?);
			"""
			res = ast.area_spherical()
			cursor.execute(insertQuery, (
				1, A, B, C, R, res, currentDateTime))
		except Exception as ex:
			print(f"Error with insert query...\n{ex}")

		connection.commit()
	except Exception as ex:
		print(f"Class exception...\n{ex}")
	print(round(ast.area_spherical()))


def show_db():
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM AST;")
	output = cursor.fetchall()
	for row in output:
		print(row)
	connection.commit()


if __name__ == "__main__":
	main()
	show_db()
	connection.close()