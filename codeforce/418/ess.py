import sys
import math
from decimal import *
sys.setrecursionlimit(30000)
def fun(alpha,n):
	if n<=0:
		return 0
	if alpha>=2:
		beta=alpha-1
		return fun(beta,n)+(n+1)*n
	beta=alpha/(alpha-1)
	#n2=int(math.floor((alpha-1)*n))
	n2=n/2
	return ((n+n2)*(n+n2+1))-fun(beta,n2)
#getcontext().prec=600
#n=int(sys.stdin.readline())
n=10**600
e=2.1
print (fun(e,n))

