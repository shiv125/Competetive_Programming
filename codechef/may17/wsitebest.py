from sys import stdin
import os.path
lookup={}
alpha='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
	lookup[i]=[]
def trieutil(blocked,unblocked):
	prefix=[]
	blocked=sorted(blocked)
	unblocked=sorted(unblocked)
	#print blocked,unblocked
	for i in unblocked:
		for j in range(26):
			if i[0]==alpha[j]:
				lookup[j].append(i)
				break
	for m in blocked:
		for j in range(26):
			if m[0]==alpha[j]:
				lookup[j].append(m)
				break
		if len(lookup[j])==1:
			prefix.append(m[0])
		else:
			temp=os.path.commonprefix(lookup[j])
	#		print temp,
			if temp==m:
				print -1
				return
			else:
				prefix.append(m[:len(temp)+1])
			lookup[j].pop()
	prefix.sort()
	store=prefix[0]
	z=[]
	z.append(store)
	count=1
	for k in range(1,len(prefix)):
		if prefix[k]!=store:
			z.append(prefix[k])
			count+=1
		store=prefix[k]
	print count
	for c in z:
		print c
		
def commonpref(str1,str2):	
	result=''
	n1=len(str1)
	n2=len(str2)
	for i in range(0,min(n1,n2)):
		if str1[i]!=str2[i]:
			break
		result+=str1[i]
	return result
	
t=1
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
		if n!='':
		    n=int(n)
		else:
		    n=0
		for i in range(n-1):
		    x=stdin.readline()
		    x=x[:len(x)-1]
		    z.append(x)
		z.append(stdin.readline())
		blocked=[]
		unblocked=[]
		z.append('')
		for line in z:
		    if len(line)!=0:
			    if line[0]=='-':
				    blocked.append(line[2:])
			    else:
				    unblocked.append(line[2:])
#		print blocked,unblocked
		if len(blocked)==0:
			print 0
		else:
			trieutil(blocked,unblocked)
	
