def fun4(arr,n,k):
	b=0
	z=0
	o=0
	ma=0
	for fr in range(n):
		if arr[fr]==0:
			z+=1
		else:
			o+=1
		if z==k:
			if z+o>ma:
				ma=z+o
		if z>k:
			while b<fr and arr[b]==1:
				b+=1
				o-=1
			if b<fr and arr[b]==0:
				b+=1
				z-=1
	return ma


def fun(arr,k,n):
	wl=wr=ml=z=sw=wz=0
	while wr<n:
		if wz<=k:
			if arr[wr]==0:
				wz+=1
			wr+=1
		else:
			if arr[wl]==0:
				wz-=1
			wl+=1
		temp=wr-wl
		if temp>ml:
			ml=temp
			sw=wl
	return ml
def fun3(arr,k,n):
	tmpK = 0
	total_so_far = 0
	max_so_far = 0
	tmpK = k
	for c in arr:
		if c == 0:
			if tmpK >= 1:
				tmpK -= 1
				total_so_far += 1
			else:
				total_so_far = 0
				tmpK = k
		elif c == 1:
			total_so_far += 1
		if max_so_far < total_so_far:
			max_so_far = total_so_far
	return max_so_far

def fun2(arr,k,n):
	mle=0
	st=0
	rl=0
	tmk=k
	for i in range(n):
		if arr[i]==1:
			rl+=1
		elif (tmk>0 and tmk<k):
			tmk-=1
			rl+=1
		elif tmk==k and k>0:
			tmk-=1
			rl+=1
			st=i
		else:
			tmk=k
			mle=max(mle,rl)
			rl=0
			tmp=i
			i=st
			st=tmp
	return max(mle,rl)
alpha='abcdefghijklmnopqrstuvwxyz'
beta={}
for i in range(26):
	beta[alpha[i]]=i
n=input()
s=raw_input()
dp=[[0 for x in range(n)] for y in range(26)]
lookup=[[0 for x in range(n)] for y in range(26)]
for i in range(26):
	for j in range(n):
		if s[j]==alpha[i]:
			lookup[i][j]=1
print lookup
		
for i in range(26):
	arr=lookup[i]
	for j in range(n):
		dp[i][j]=fun4(arr,j,n)
print str(dp[14][1])+'sd'
q=input()
for i in range(q):
	ma,ch=map(str,raw_input().split())
	ma=int(ma)
	print dp[beta[ch]][ma]

