t=input()
while t>0:
	t-=1
	K=input()
	P=[0]*K
	S=[0]*K
	for i in range(K):
		P[i],S[i]=map(int,raw_input().split())
	N=input()
	if N==1:
		D,M=map(int,raw_input().split())
		mi=10000
		for i in range(K):
			if P[i]*M>=D:
				mi=min(mi,S[i])
		if mi==10000:
			mi=-1
		print mi
	else:
		break
		
