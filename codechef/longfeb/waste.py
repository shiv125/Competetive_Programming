import timeit
c=0
start = timeit.default_timer()
for i in range(2*10**7):
	c+=1
#Your statements here

stop = timeit.default_timer()

print stop - start 
