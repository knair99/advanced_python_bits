
def area(*args):
	print len(args)
	print type(args)
	print args

	i = iter(args)
	v  = next(i)

	for each in i:
		v *= each
		print each
		print v

	return v

area(10,100, 100)


def tags (*args, **kwargs):
	print args
	print kwargs
	print type(kwargs)


tags(1, 2, src="C:\\", location="file://C:\\")