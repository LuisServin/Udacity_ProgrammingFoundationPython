# !usr/bin/env python

class Parent():
	"""docstring for Parent"""
	def __init__(self, last_name, eye_color):
		print "Parent constructor called"
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print "Last name -- " + self.last_name
		print "Eye Color -- " + self.eye_color

# using inheritance to reuse the code in Parent class
class Child(Parent):
	"""docstring for Child"""
	def __init__(self, last_name, eye_color, number_of_toys):
		print "Child constructor called"
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

	# we override the method from the Parent class to redefine it in
	# this class
	def show_info(self):
		print "Last name -- " + self.last_name
		print "Eye Color -- " + self.eye_color
		print "Numer of toys -- " + str(self.number_of_toys)
		
billy_cyrus = Parent("Cyrus","blue")
billy_cyrus.show_info()

milley_Cirus = Child("Cyrus","blue",5)
milley_Cirus.show_info()