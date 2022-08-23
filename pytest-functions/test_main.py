import pytest


def setup_module():
	...


def teardown_module():
	...

def test_upper():
	assert 'foo'.upper() == 'FOO'


def test_is_upper():
	assert 'foo'.isupper()


def test_is_upper():
	assert 'FOO'.isupper()


def test_failed_upper():
	assert 'foo'.upper() == 'FOo'



