# cook your code here
import sys
for s in sys.stdin:
	counta=0
	countb=0
	flag=0
	a=0
	b=0
	c=5
	d=5
    ind=0
	for i in range(10):
		if (i%2==0):
			c-=1
			if s[i]=='1':
				a+=1
		else:
			d-=1
			if s[i]=='1':
				b+=1
		if (a-b)>d:
			flag=1
			ind=i+1
			print 'TEAM-A '+str(ind)
			break
		elif (b-a)>c:
			ind=i+1
			print 'TEAM-B '+str(ind)
			break
	if flag==0:
		#tie
		for i in range(10,19,2):
			j=i+1
			if s[i]=='1':
				counta+=1
			if s[j]=='1':
				countb+=1
			if counta>countb:
				flag=1
				print 'TEAM-A '+str(j+1)
				break
			elif counta<countb:
				flag=1
				print 'TEAM-B '+str(j+1)
				break
	if flag==0:
		print 'TIE'


