

class Symbol:
	
	def __init__(self):
		"""
		Initialise object 
		Initialise the attribute _icon and _color
		"""
		self._icon = ["HEARTS", "DIAMOND", "CLUBS", "SPADES"]
		self._color = ["red", "black"]	

	#getter icon
	@property
	def get_icon(self):

		return self._icon

	#getter colors
	@property	
	def get_color(self):
		return self._color


	#printing the object
	def __str__(self):
		retrun(self._icon)


#child class, inherence from Symbol class
class Card(Symbol):
	
	#initilise oject
	def __init__(self):
		"""
		initilise the object
		initilise the attribute _value
		"""
		super().__init__()
		self._value = ['A', '2', '3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	
	#getter value 
	@property
	def get_value(self):
		return self._value	

	#print object
	def __str__(self):
		retrun(self._value)
	
