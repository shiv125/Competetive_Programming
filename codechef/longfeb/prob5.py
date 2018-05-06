def interval(i,j,A,bk):
	curr_max=0
	i_adv=0
	j_adv=0
	m=i
	for m in range(i+1,i+bk+1):
		curr_max+=A[m]
	i_adv=i+1
	j_adv=m
	ovm=curr_max
	for m in range(i+1,j-bk):
		curr_max=curr_max+A[m+bk]-A[m]
		if ovm<curr_max:
			ovm=curr_max
			i_adv=m+1
			j_adv=m+bk
			#curr_max=curr_max+A[m+bk]-A[m]
	return i_adv,j_adv,ovm
t=input()
for i in range(t):
	N,M=map(int,raw_input().split(" "))
	A=map(int,raw_input().split(" "))
	B=map(int,raw_input().split(" "))
	max_=0
	total=0
	l=-1
	r=N
	for i in range(M):
		l,r,max_=interval(l,r,A,B[i])
		print l,r
		if i%2==0:
			total+=max_
		else:
			total-=max_

	print total

