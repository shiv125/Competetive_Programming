import math
from decimal import *
getcontext().prec=14
t=input()
res=[]
while t>0:
	t-=1
	H,S=map(Decimal,raw_input().split())
	#H=Decimal(H)
	#S=Decimal(S)
	y= H*H-Decimal(4)*S
	if y<0:
		print -1
	else:
		x=H*H+Decimal(4)*S
		x=x**Decimal(0.5)
		y=y**Decimal(0.5)
		if x<=H:
			print -1
		else:
			print (x-y)/Decimal(2),(y+x)/Decimal(2),H
	
