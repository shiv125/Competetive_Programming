def fun(arr):
	sum_=0
	for i in range(1,16):
		sum_=0
		for k in range(4):
			z=1
			z=z<<k
			if i&z:
				sum_+=arr[k]
				if sum_==0:
					return "Yes"
	return "No"
t=input()
while t>0:
	t-=1
	arr=map(int,raw_input().split())
	print fun(arr)
	
