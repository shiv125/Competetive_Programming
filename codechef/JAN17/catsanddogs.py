t=input()
Leg=[0]*t
for i in range(t):
	C,D,L=map(int,raw_input().split(' '))
	k=(L-4*D)/4
	if (((L-4*D)%4==0) and k>=0):
		if (C<=2*D and k<=C):
			Leg[i]=1
			
		else:
			if (k<=C and k>=C-2*D):
				Leg[i]=1
			
for i in range(t):
	if (Leg[i]==1):
		print "yes"
	else:
		print "no"
