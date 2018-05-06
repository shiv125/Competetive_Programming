def fun(h,a,flag):
	if h<=0 or a<=0 or h>=MAX or a>=MAX:
		return 0
	if flag==0:#air
		if dp0[h][a]<0:
			dp0[h][a]=max(fun(h-5,a-10,1)+1,fun(h-20,a+5,2)+1)
		return dp0[h][a]
	elif flag==1:#water
		if dp1[h][a]<0:
			dp1[h][a]=max(fun(h+3,a+2,0)+1,fun(h-20,a+5,2)+1)
		return dp1[h][a]
	else:#fire
		if dp2[h][a]<0:
			dp2[h][a]=max(fun(h-5,a-10,1)+1,fun(h+3,a+2,0)+1)
		return dp2[h][a]
MAX=10**3+10
t=input()
while t>0:
	t-=1
	H,A=map(int,raw_input().split())
	dp0=[[-1 for x in range(MAX)] for y in range(MAX)]
	dp1=[[-1 for x in range(MAX)] for y in range(MAX)]
	dp2=[[-1 for x in range(MAX)] for y in range(MAX)]

	H+=3
	A+=2
	print fun(H,A,0)

