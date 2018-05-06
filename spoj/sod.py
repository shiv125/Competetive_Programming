MAX=10**6+2
dp=[0]*MAX
y=13500#till 999
dp[0]=13500
l=0
for i in range(1,1000):
	while i>0:
		l+=i%10
		i/=10
for i in range(1,10**6):
	l=0
	m=i
	while i>0:
		l+=i%10
		i/=10
	dp[m]=dp[m-1]+(l)*1000+13500
while True:
	a,b=map(int,raw_input().split())
	if a==-1 and b==-1:
		break
	ind1=a/1000
	ind2=b/1000
	z=(ind1+1)*1000
	z1=ind2*1000
	total=0
	if ind1==ind2:
		for i in range(a,b+1):
			while i>0:
				total+=i%10
				i/=10
	else:
		if ind1!=0 and ind2!=0:
			total+=dp[ind2-1]-dp[ind1]
		elif ind1==0 and ind2!=0:
			total+=dp[ind2-1]-dp[0]
		for i in range(a,z):
			while i>0:
				total+=i%10
				i/=10
		for i in range(z1,b+1):
			while i>0:
				total+=i%10
				i/=10
	print total
