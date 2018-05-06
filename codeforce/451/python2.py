n=input()
a=input()
b=input()
flag=0
for y in range(n+1):
	if (n-b*y)>=0 and (n-b*y)%a==0:
		flag=1
		ans1=(n-b*y)/a
		ans2=y
if flag:
	print "YES"
	print ans1,ans2
else:
	print "NO"
