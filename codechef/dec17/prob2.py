import sys
#for s in sys.stdin:
while True:
	s=raw_input()
	if s=='':
		break
	counta=0
	countb=0
	flag=0
	for i in range(0,9,2):
		j=i+1
		if s[i]=='1':
			counta+=1
		if counta-countb>=10-i:
			flag=1
			print 'teama'+str(i)
			break
		if s[j]=='1':
			countb+=1
		if countb-counta>=9-i:
			flag=1
			print 'TEAM-B ' +str(j)
			break
		#if counta-countb>=9-i:
		#	flag=1
		#	print 'TEAM-A '+str(i)
		#	break
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

			
