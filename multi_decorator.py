#now lets make another decorator
#first define decorator function that takes as argument a function
def toupper(f):

	#implement the decoration function
	def convert(*args, **kwargs):
		value = f(*args, **kwargs) 
		return value.upper()

	#returns the function
	return convert


#third decorator
class Logger:
	def __init__(self):
		pass

	def __call__(self, f):
		def wrapper(*args, **kwargs):
			print "Log>>"
			return f(*args, **kwargs)
		return wrapper

#lets also decorate with an instance object
logger = Logger()


#you can have multiple decorators
#now apply class as decorator to function
@logger
@toupper
def Greeting():
	return "Hello there"


for i in range(0,10):
	print Greeting()