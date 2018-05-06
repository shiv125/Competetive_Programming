#x=['1100','0011','1010','1000']
#x=sorted(x)
#x=['111','001','010']
x=["11101", "00111", "10101", "00000", "11000"]
n=len(x)
m=len(x[0])
countz=[]
lookup=[0]*m
counters=[0]*n
for i in range(n):
	count=0
	for j in range(m):
		if x[i][j]=='1':
			count+=1
	countz.append([i,count])

countz.sort(key=lambda x: x[1])
result=0
print countz

for i in countz:
	j=i[0]#considering jth string first
	for y in range(m):
		if x[j][y]=='1' and lookup[y]!=1:
			lookup[y]=1
			counters[j]+=1
	result+=(counters[j])**2	
print counters
print result
