import sqlite3
import json


class features:
	def __init__(self):
		self.path = 'userData/data.db'

	def create_database(self):
		try:

			connection = sqlite3.connect(self.path)
			cur = connection.cursor()

			cur.execute("CREATE TABLE stack (data json)")

			connection.commit()
			connection.close()

			return 0

		except :

			return 1

	def add_to_stack(self,data):

		if id != '':

			connection = sqlite3.connect(self.path)
			cur = connection.cursor()

			cur.execute("INSERT INTO stack VALUES (?)",[json.dumps(data)])

			connection.commit()
			connection.close()

			return 1

		else:

			return 0

	def fetch_stack(self):

		try:
			connection = sqlite3.connect(self.path)
			cur = connection.cursor()

			cur.execute("SELECT * FROM stack")
			data = cur.fetchall()
			jsonifyed = []

			connection.commit()
			connection.close()

			for i in data:
				jsonifyed.append(json.loads(i[0]))

			return jsonifyed

		except:

			return 0