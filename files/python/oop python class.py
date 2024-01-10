class Car():
	"""A simple attempt to model a Car."""
	def __init__(self, name, colour):
		"""Initializing name, colour and model attributes."""
		self.name = name
		self.colour = colour
	def get_Speed(self):
		"""Setting the speed of the car."""
		print("Top speed of " + self.name + " is 150 km/hr and " + self.colour) 

# Creating an instance/object called Honda_City
Honda_City = Car("Honda City","Red")
# Calling the method using the name of the instance
Honda_City.get_Speed() 