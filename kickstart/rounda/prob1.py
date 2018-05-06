mod=10**9+7
#f=[1]*10**
#f[1]=0
#for i in range(2,1001):
#	f[i]=f[i-1]+i*(i-1)*(2*i-1)/6
#	f[i]=f[i]%mod
def f4(i):
	a=(i*(i+1))%mod
	b=(2*i+1)%mod
	c=(3*(i*i)+3*i-1)%mod
	return ((a*b*c)/30)%mod
def f2(i):
	return ((i*(i+1)*(2*i+1))/6)%mod

def f(i):
	k=i**2
	r=(i**2-1)%mod
	return ((k*r)/12)%mod
def common(min_,max_):
	t=min_-1
	n=max_-min_
	result=0
	indi=1
	j=0
	if t%2==0:
		teven=(t/2)
	else:
		teven=(t-1)/2
	result=(f2(t)-f4(t)-2*(4*f2(teven)-16*f4(teven)))%mod
	''''
	while t>1:
		if j%2==0:
			indi=1
		else:
			indi=-1
		result+=2*indi*f(t)
		t-=1
		j+=1
	'''
	result=((n*result)/6)%mod
	return result
def compute(r,c):
	k=min(r,c)
	y=max(r,c)
	n=y-k+1
	ans=(n*f(k))%mod-common(k,y)
	#ans=n*f(k)
	return (ans)%mod
'''
myout=open("output.txt","w")
with open("large-file.txt","r") as x:
	inp=[]
	for line in x:
		inp.append(line)
inp=[x.strip() for x in inp]
t=int(inp[0])
'''
t=1
for i in range(1,t+1):
	r,c=map(int,raw_input().split())
	k=compute(r,c)
	print k
	#myout.write("Case #"+str(i)+": "+ str(k)+"\n")

