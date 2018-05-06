n=input()
res=set('abcdefghijklmnopqrstuvwxyz')
r=n-2
for i in range(n-1):
	x,s=raw_input().split()
	y=set(s)
	if x=='!':
		res=res.intersection(y)
	else:
		res=res.difference(y)
	if len(res)==1:
		r=i
		break
count=0
for j in range(r+1,n-1):
	x,s=raw_input().split()
	if x!='.':
		count+=1
w=raw_input().split()		
	
print count
