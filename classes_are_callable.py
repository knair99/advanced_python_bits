def create_sequence(immutable):
	if immutable:
		return tuple
	else:
		return list


seq = create_sequence(True)
instance = seq("hello")
print instance

#check if callable
print callable(instance)


class Cat:
	def __init__(self, name):
		self.name = name

	def __call__(self): #making it a callable class
		print "hi my name is ", self.name

kitty = Cat("kitty")
kitty() #__call__ now makes this a callable instance

print Cat("hi")()