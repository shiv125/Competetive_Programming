n,k=map(int,raw_input().split())
arr=[]
count={}
for i in range(n):
	arr.append(input())
	count[arr[i]]=1
#count=[0]*MAX
#for i in range(n):
#	count[arr[i]]=1
total=0
arr.sort()
for i in range(n):
	if arr[i]+k in count:
		total+=1
print total
