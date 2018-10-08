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

class Der(Gas):
	size = 5

g1= Der()

# print(help(Der()))
print(g1.size)