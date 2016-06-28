

#decorator
def convert_toupper(f):

	def convert(*args, **kwargs):
		value = f(*args, **kwargs) 
		return value.upper()

	return convert



@convert_toupper
def already_existing_function():

	return "lowercase string"


print already_existing_function()