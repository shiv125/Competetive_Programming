import timeit
start_time = timeit.default_timer()
count=0
b=0
c=0
for i in range(*10**7):
	count+=1
	b=b+2
	c-=1
print count
elapsed = timeit.default_timer() - start_time
print elapsed
