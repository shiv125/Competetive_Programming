from sys import stdin
def commonpref(str1,str2):	
	result=''
	n1=len(str1)
	n2=len(str2)
	for i in range(0,min(n1,n2)):
		if str1[i]!=str2[i]:
			break
		result+=str1[i]
	return result
	
t=10
r12=0
for i in range(t):
	#n=raw_input()
	if r12==1:
		print -1
	else:
		z=[]
		n=stdin.readline()
		for r in range(len(n)):
		    if n[r]=="\n":
		        n=n[:r]
		        break
	#	print n
		if n!='':
		    n=int(n)
		else:
		    n=0
		#n=int(n)
		for i in range(n-1):
		    x=stdin.readline()
		    x=x[:len(x)-2]
		    z.append(x)
		z.append(stdin.readline())
	#		print z
	#	print z
		blocked=[]
		unblocked=[]
		z.append('')
		q=0
		for line in z:
		    if len(line)!=0:
			    if line[0]=='-':
				    blocked.append(line[2:])
			    else:
				    unblocked.append(line[2:])
		r=[]	
		n1=len(unblocked)
		n2=len(blocked)
		for i in range(n2):
			r.append(0)
		y=[]
		for i in range(n2):
			result=""
			for j in range(n1):
				s=commonpref(blocked[i],unblocked[j])
				if len(s)>len(result):
					result=s
			if result==blocked[i]:
				r[i]=-1
			else:
				k=len(result)
				result+=blocked[i][k]
				y.append(result)
		count=0
		for i in range(n2):
			if r[i]==-1:
				count+=1
		if count==0:
			te=set()
			for i in range(n2):
				te.add(y[i])
			print len(te)
		#	print te
			te=sorted(te)
			#print te
			for i in te:
				print i
		else:
			print "-1" 

