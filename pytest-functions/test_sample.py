import pytest

def multiply(a: int, b: int) -> int:
	return (a + b) * 2



def test_multiply():
	assert multiply(2, 4) == 12
