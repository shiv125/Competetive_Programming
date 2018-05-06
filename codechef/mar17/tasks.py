t=input()
for i in range(t):
	N=input()
	xenny=map(int,raw_input().split(" "))
	yanna=map(int,raw_input().split(" "))
	even=0
	odd=0
	for i in range(N):
		if i%2==0:
			even+=xenny[i]
		else:
			even+=yanna[i]
	for i in range(N):
		if i%2!=0:
			odd+=xenny[i]
		else:
			odd+=yanna[i]
	print min(even,odd)

	

