

#x:			1	2	3	4	5	6	7	
#fib(x):	1	1	2	3	5	8	13
#fib(x) = fib(x-1) + fib(x-2)

def fib(x):

	if x <= 2 :
		return 1

	result = fib(x-1) + fib(x-2)
	return result


print fib(7)


def add_data(*args):
	
	sum1 = 0 
	for each in args:
		sum1 = sum1 + each
	print args

	lis = list(args)
	print lis
	lis.append(sum1)
	return lis

print add_data(30, 50, 60)

def draw_pic(*args,**kwargs):
	print args
	print kwargs

draw_pic (120, 240, "kk", src="C:\\", location="http://google.com")


def pass_fun(xyz):

	print "executing"
	print len(xyz)


pass_fun(range(10,100))
pass_fun([])
pass_fun({"src": "source"})
pass_fun("kk nair")