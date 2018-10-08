# classMethods and staticmethod

class Gas:
	size = 1

	def __init__(self):
		self.name = None
		# self.size = 1

	@classmethod
	def change_size(cls, amount):
		cls.size = amount

	@classmethod
	def form_string(cls, tense):
		parse = tense
		return parse

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return True
		return False


g1= Gas()
Gas.change_size(3)
print(g1.size)

import datetime

my_day = datetime.date(2018, 10, 5)
print(Gas.is_workday(my_day))

