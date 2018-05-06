t=input()
alpha='abcdefghijklmnopqrstuvwxyz'
while t>0:
	t-=1
	#locs=[[0 for x in range(n)] for y in range(26)]
	inp=raw_input()
	k=input()
	temp=[]
	temp.append(inp[0])
	n=len(inp)
	p=1
	for i in range(1,n):
		while p>=1:
			if i-p<n-k and temp[-1]>inp[i]:
				temp.pop()
				p-=1
			else:
				break
		if p<k:
			temp.append(inp[i])
			p+=1	
	print ''.join(temp)

