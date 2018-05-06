n=input()
s=raw_input()
d='ABCD'
res=[]
for i in range(0,2*n,2):
	a=s[i]
	b=s[i+1]
	for j in d:
		if j!=a and j!=b:
			res.append(j)
for i in range(2,2*n-1,2):
	if res[i]==res[i-1]:
		temp=res[i+1]
		res[i+1]=res[i]
		res[i]=temp
print ''.join(res)	

