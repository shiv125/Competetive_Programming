import sys
import math
import decimal
decimal.setcontext(decimal.Context(prec=1000))
n=decimal.Decimal(sys.stdin.readline())
alpha=decimal.Decimal(1).exp()
ans=0
j=0
n2=0
while n>0:
	j+=1
	while alpha>=2:
		alpha=alpha-decimal.Decimal(1)
		if j%2!=0:
			ans=ans+float(((n+1)*n)/2)
		else:
			ans=ans-float(((n+1)*n)/2)
	else:
		n2=math.floor((alpha-decimal.Decimal('1'))*decimal.Decimal(n))
		if j%2==0:
			ans-=float(((n+n2)*(n+n2+1))/2)
		else:
			ans=ans+float(((n+n2)*(n+n2+1))/2)
		alpha=decimal.Decimal(alpha)/(alpha-decimal.Decimal('1'))
	n=n2
ans=int(ans)
sys.stdout.write(str(ans)+"\n")

