import time
start=time.clock()
def sieve(MAX,all_primes):
	prime=[True for i in range(MAX+1)]
	p=2
	while p*p<=MAX:	
		if prime[p]==True:
			for i in range(p*2,MAX+1,p):
				prime[i]=False
		p+=1
	for p in range(2,MAX):
		if prime[p]==True:
			all_primes.append(p)
def binarysearch(arr,low,high,x):
	if x>arr[high]:
		return -1
	while high-low>1:
		mid=(low+high)/2
		if arr[mid]>=x:
			high=mid
		else:
			low=mid
	return high
def binarysearchfloor(arr,low,high,x):
	if x<arr[0]:
		return -1
	while high-low>1:
		mid=(low+high)/2
		if arr[mid]<=x:
			low=mid
		else:
			high=mid
	
	return low

with open('testc2.txt',"r") as f:
	inp=[]
	for line in f:
		inp.append(line)

inp=[x.strip() for x in inp]
MAX=10**6+2
MAP=78498
primes=[x for x in range(MAX)]
for i in range(4,MAX,2):
	primes[i]=2
i=3
while i*i<MAX:
	if primes[i]==i:
		j=i*i
		while j<MAX:
			if primes[j]==j:
				primes[j]=i
			j+=i
	i+=1
all_primes=[]
sieve(MAX,all_primes)
dic={}
tt=len(all_primes)
for i in range(tt):
	dic[all_primes[i]]=i

#print time.clock()
#print all_primes
#n=int(inp[0])
n=6
#arr=list(map(int,inp[1].split()))
arr=[25,12,18,6,8,9]
#m=int(inp[2])
m=3
lookup={}

dp=[[0 for x in range(n)] for y in range(70)]
#for i in range(n):
#	lookup[i]=[]
special=[]
'''
for i in range(70):
	pri=all_primes[i]
	count=0
	for j in range(n):
		while arr[j]%pri==0:
			arr[j]=arr[j]/pri
			count+=1
		dp[i][j]+=count
'''

for i in range(n):
	elem=arr[i]
	curr=primes[elem]
	count=1
	total=0
	while elem>1 and primes[elem]<340:
		elem=elem//primes[elem]
		if curr==primes[elem]:
			count+=1
			continue
		total+=count
		dp[dic[curr]][i]+=total
		if dic[curr]>0:
			dp[dic[curr]][i]+=dp[dic[curr]-1][i]
		curr=primes[elem]
		count=1

	#if i>0:
	#	dp[i]+=dp[i-1]
	if elem>1:
		special.append([elem,i])
print dp
print 
print
for j in range(1,n):
	for i in range(70):
		dp[i][j]+=dp[i][j-1]
print dp


'''
#for i in range(70):
#	for j in range(1,n):
#		dp[i][j]+=dp[i][j-1]
#for i in range(n):
#	for j in range(1,70):
#		dp[j][i]+=dp[j-1][i]
#print time.clock()-start
'''
'''
for i in range(m):
	L,R,X,Y=map(int,inp[i+3].split())
	fi=binarysearch(all_primes,0,tt-1,X)
	si=binarysearchfloor(all_primes,0,tt-1,Y)
	
	#print (fi,si)
	ans=0
	if fi!=-1:
		l_b=(L-1)//bucket
		r_b=(R-1)//bucket
	#	print (l_b,r_b)
		
		if r_b-l_b<=1:
			for j in range(L-1,R):
				for k in range(len(lookup[j])):
					if lookup[j][k][0]>=X and lookup[j][k][0]<=Y:
						ans+=lookup[j][k][1]
					if lookup[j][k][0]>Y:
						break
	#		print (ans)

		if r_b-l_b>1:
			if fi!=0:
				ans+=dp[si][r_b-1]-dp[si][l_b]-(dp[fi][r_b-1]-dp[fi][l_b])
			else:
				ans+=dp[si][r_b-1]-dp[si][l_b]
			R1=(l_b+1)*bucket
	#		print (ans)
			
			for j in range(L-1,R1):
				for k in range(len(lookup[j])):
					if lookup[j][k][0]>=X and lookup[j][k][0]<=Y:
						ans+=lookup[j][k][1]
					if lookup[j][k][0]>Y:
						break
			L2=(r_b)*bucket
			
	#		print (ans)
	#		print (R1,L2)
			for j in range(L2,R):
				for k in range(len(lookup[j])):
					if lookup[j][k][0]>=X and lookup[j][k][0]<=Y:
						ans+=lookup[j][k][1]
					if lookup[j][k][0]>Y:
						break
		#print (ans) 
	
	'''
print time.clock()-start
