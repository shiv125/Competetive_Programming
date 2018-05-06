def lcm(a,b):
	if (a>b):
		t=a
	else:
		t=b
	while True:
		if ((t%a==0) and (t%b==0)):
			y=t
			break
		t+=1
	return y


n,m,z=map(int,raw_input().split(" "))
k=lcm(n,m)

print z/k

