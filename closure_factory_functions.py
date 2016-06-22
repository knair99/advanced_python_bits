
#closures can be used to implement a factory function
#a function that returns other useful functions, specialized in some way
#by using closure

#this is a factory function
def raised_to(x): #x will be "closed over"

	def raise_it(y): #this will now have access over x following the LEGB rule
		return pow(y,x) #this is the actual work of a function

	return raise_it # we return a function making this a factory function 


#now we can easily create functions
cube = raised_to(3)
print cube(5)

square = raised_to(2)
print square(5)