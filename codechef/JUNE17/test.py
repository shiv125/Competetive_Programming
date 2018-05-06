import time
c=0
st=time.clock()
for i in range(6*10**7):
	c+=1
print c
print time.clock()-st
