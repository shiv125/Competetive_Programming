def search(x,look):
	low=0
	high=len(look)-1
	if len(look)==0:
		return -1
	while low<=high:
		if x<=look[low][0]:
			return low
		if x>look[low][0]:
			return -1
		mid=(low+high)/2
		if look[mid][0]==x:
			return mid
		elif look[mid][0]<x:
			if mid+1<=high and x<=look[mid+1][0]:
				return mid+1
			else:
				low=mid+1
		else:
			if mid-1>=low and x>=look[mid-1][0]:
				return mid
			else:
				high=mid-1
	return -1

def searchfloor(x,look):
	low=0
	high=len(look)-1
	if len(look)==0:
		return -1
	while low<=high:
		if x>=look[high][0]:
			return high
		mid=(low+high)/2
		if look[mid][0]==x:
			return mid
		if mid>0 and look[mid-1][0]<=x and x<look[mid][0]:
			return mid-1

		if x<look[mid][0]:
			high=mid-1
		if x>look[mid][0]:
			low=mid+1
		
	return -1	
	
n,x=map(int,raw_input().split())
inp=[]
lookup={}
lookup2={}
for i in range(2*10**5+5):
	lookup[i]={}
	lookup2[i]=[]
for i in range(n):
	l,r,c=map(int,raw_input().split())
	inp.append([l,r,c])
	diff=r-l+1
	if l in lookup[diff]:
		lookup[diff][l]=min(lookup[diff][l],c)
	else:
		lookup[diff][l]=c
for i in lookup:
	#lookup[i].sort(key=lambda: x:x[0])
	for j in lookup[i]:
		lookup2[i].append([j,lookup[i][j]])
for i in lookup2:
	lookup2[i].sort(key=lambda x:x[0])
mi=1000000000
flag=False
for i in range(1,x/2+1):
	for j in lookup2[i]:
		fi=search(j[0]+i,lookup2[x-i])
		if fi!=-1 and (j[0]+i-1)!=lookup2[x-i][fi][0]:
			cost=lookup2[x-i][fi][1]+j[1]
			mi=min(cost,mi)
			flag=True
		fi=searchfloor(j[0]-i,lookup2[x-i])
		if fi!=-1 and j[0]!=lookup2[x-i][fi][0]+x-i-1:
			cost=lookup2[x-i][fi][1]+j[1]
			mi=min(cost,mi)			
			flag=True
if flag:
	print mi			
else:
	print -1
