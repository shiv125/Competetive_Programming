def fun(n):
	if n<=9:
		return n*n
	k=n/9
	res=81*k
	r=n%9
	for i in range(1,r+1):
		res+=(2*i-1)
	return res
while True:
	try:
		n=input()
		print fun(n)
	except (EOFError):
		break






