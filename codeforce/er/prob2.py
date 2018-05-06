n=input()
arr=map(int,raw_input().split())
f3=0
f2=0
arr.sort()
if arr[0]==arr[1] and arr[1]==arr[2]:
	f3=1
if arr[0]==arr[1] or arr[1]==arr[2]:
	f2=1
count=0
if f3:
	for i in range(n):
		if arr[i]==arr[0]:
			count+=1
		else:
			break
	print max((count*(count-1)*(count-2))/6,1)
else:
	if f2==1:
		if arr[1]==arr[2]:
			for i in range(1,n):
				if arr[i]==arr[1]:
					count+=1
			print max((count*(count-1))/2,1)
		else:
			for i in range(2,n):
				if arr[i]==arr[2]:
					count+=1
			print max((count*(count-1))/2,1)
	else:
		for i in range(2,n):
			if arr[i]==arr[2]:
				count+=1
		print max(count,1)
