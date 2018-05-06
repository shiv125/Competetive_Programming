def nice(arr):
	n=len(arr)
	if (arr[1]-arr[0])>1:
		return arr[0]
	elif (arr[n-1]-arr[n-2]>1):
		return arr[n-1]
	else:
		for i in range(n):
			if arr[i]==arr[i-1]:
				return arr[i]
t=input()
result=[]
for i in range(t):
	N=input()
	arr=map(int,raw_input().split(" "))
	arr=sorted(arr)
	result.append(nice(arr))
for i in result:
	print i
