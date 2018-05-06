n=input()
lookup={}
lookup[2]=[6,2,4,8]
lookup[3]=[1,3,9,7]
lookup[4]=[6,4]
lookup[9]=[1,9]
lookup[8]=[6,8,4,2]
lookup[7]=[1,7,9,3]
for i in range(n):
	a,b=map(str,raw_input().split())
	b=int(b)
	l=int(a[-1])
	if b==0:
		if len(a)==1 and l==0:
			print 0
		else:
			print 1
	else:
		if l==1 or l==0 or l==5 or l==6:
			print l
		else:
			if l==4 or l==9:
				r=b%2
				print lookup[r]
			else:
				r=b%4
				print lookup[l][r]

