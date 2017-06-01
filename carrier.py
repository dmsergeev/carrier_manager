class Carrier:
	def __init__(self, name, _id):
		self.name = name
		self._id = _id

	def __str__(self):
		return "Carrier " + self.name

	def get_name_capitalize(self):
		return self.name.capitalize()

	def get_carrier_name(self):
		return self.name