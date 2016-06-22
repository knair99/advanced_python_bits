

sunday  = [1,2,3,4,5]
monday  = [10,20,30,40,50]
tuesday = [100,200,300,400,500]

print "sunday = ", sunday
print "monday = ", monday
print "tuesday = ", tuesday

hourlies = zip(sunday, monday, tuesday)

print hourlies

daily = [sunday, monday, tuesday]
print daily

print zip(daily)
print zip(*daily)
print list(zip(*daily))

for item in zip(*daily):
	print "hourly avg temp all three days", float(sum(item)/3)