n,k=map(int,raw_input().split())
arr=map(int,raw_input().split())
total=0
days=0
rest=0
for i in range(n):
	rest+=arr[i]
	if total>=k:
		break
	if rest>8:
		total+=8
		rest-=8
	else:
		total+=rest
		rest=0
	days+=1
if total>=k:
	print days
else:
	print -1
