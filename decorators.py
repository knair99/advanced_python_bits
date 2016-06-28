

#decorator
#first define decorator function that takes as argument a function
def convert_toupper(f):

	#implement the decoration function
	def convert(*args, **kwargs):
		value = f(*args, **kwargs) 
		return value.upper()

	#returns the function
	return convert


#prefix already existing function with decorator
@convert_toupper
def already_existing_function():

	return "lowercase string"


print already_existing_function()

