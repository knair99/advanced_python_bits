

class FunctionCounter:

	#ctor must be capable of taking a function
	def __init__(self, f):
		self.f = f
		self.count = 0

	#make it callable to be used as decorator
	def __call__(self, *args, **kwargs):
		self.count += 1
		return self.f(*args, **kwargs)



#now apply class as decorator to function
@FunctionCounter
def Greeting():
	print "Hello there"


for i in range(0,10):
	Greeting()
	print Greeting.count



