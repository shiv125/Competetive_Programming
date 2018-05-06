n=input()
def fun(n):
	lookup={}
	lookup[1]='a'
	lookup[2]='aa'
	lookup[3]='aab'
	lookup[4]='aabb'
#	lookup[5]='aabba'
#	lookup[5]='aabbaa'
	#lookup[6]='aabbac'
	string=''
	x=n/4
	y=n%4
	for m in range(x):
		string+=lookup[4]
	if y!=0:
		string+=lookup[y]
	#print len(string)
	print string	
fun(n)
#for i in range(1,n+1):
	
#for i in range(1,14):
#	fun(i)
