def mul(s,k):
	n=len(s)
	res=[0]*n+1
	c=0
	for i in range(n-1,-1,-1):
		res[i]=(int(s[i])%10)+c
		c=int(s[i])/10
	res[0]=c
	return res
n=input()
for i in range(n):
	l,r=map(str,raw_input().split())
	lookup={}
	for j in range(1,9):
		lookup[i]=mul(l,j)
	lookup[0]=[0]*(len(l)+1)
	res=[0]*(len(l)+len(r))
	t=len(l)+len(r)-1
	for j in range(len(r)-1,-1,-1):
		su+=lookup[int(r[j])]
	

	print l*r




