
#this one is nested
l = [(x,y) for x in range (0,10) for y in range (0,5)]

print l

# a comprehension within a comprehension
l = [ [x for x in range (y)] for y in range (0,5)]
#generate all subsets of a range
print l

str1 = "abcde"
expanding_strings = [ [x for x in str1[0:y+1]] for y in range (0, len(str1))]
print expanding_strings

#same as writing
strings = []
for y in range(0, len(str1)):
	for x in str1[0:y+1]:
		strings.append(x)
	print strings
