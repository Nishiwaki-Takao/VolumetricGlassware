from typing import Literal

CapInJIS: Literal[float] = Literal[ 0.1, 0.2, 0.3, 0.4, 0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 17.5, 17.6, 20, 25, 30, 40, 50, 100, 200 ]

def theCapInJIS(value):
	try:
		value in CapInJIS
	except:
		ValueError('the capacity value is out of JIS')
	else:
		return value
		


