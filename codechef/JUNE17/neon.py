t=input()
z=[]
while t>0:
	t-=1
	N=input()
	arr=map(int,raw_input().split())
	t1=0
	t2=0
	c=0
	neg_arr=[]
	pos_arr=[]
	for i in range(N):
		if arr[i]<0:
			t1+=arr[i]
			neg_arr.append(arr[i])
		else:
			t2+=arr[i]
			pos_arr.append(arr[i])
			c+=1
	neg_arr=sorted(neg_arr,reverse=True)
	pos_arr.sort()
	lp=len(pos_arr)
	ln=len(neg_arr)
	p=0
	total1=lp*t2
	total2=0
	while p<ln:
		total=max(t2*lp,(t2+arr[p])*(lp+1))
		if t2*lp<(t2+arr[p])*(lp+1):
			lp+=1
		else:
			total2+=arr[p]
		p+=1
	z.append(total1+total2)
for i in z:
	print i

