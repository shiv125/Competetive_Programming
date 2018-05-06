def rev(n):
	a=0
	val=0
	while n>0:
		a*=10
		a+=n%10
		val+=1
		n/=10
	return a,val
	
k,p=map(int,raw_input().split())
tot=0
for i in range(1,k+1):
	re,po=rev(i)
	tot=(tot+i*10**po+re)%p
print tot
	
