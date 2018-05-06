MAX=10**6+10**5+4
fib=[0]*MAX
fib[1]=1
mod=10**5
temp=[0]*100
for i in range(2,MAX):
	fib[i]=(fib[i-1]+fib[i-2])%mod
t=input()
while t>0:
	t-=1
	a,b=map(int,raw_input().split())
	ma=-1
	for i in range(a,a+100):
		temp[i]=fib[i]
		if mi<temp[i]:
			mi=temp[i]
	res=[]
	for i in range(a+100,a+b+1):
		if fib[i]<mi:
			temp.remove(mi)
			temp.append(fib[i])
	
	


	
