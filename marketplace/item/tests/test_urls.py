import unittest
from django.test import Client


class UrlsTest(unittest.TestCase):
	def setUp(self):
		self.client = Client()

	def test_home_item(self):
		response = self.client.get('')
		self.assertEqual(response.status_code, 200)

	def test_new_item(self):
		response = self.client.get('/items/new/')
		self.assertEqual(response.status_code, 302)



