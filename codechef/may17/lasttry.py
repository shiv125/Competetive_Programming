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
				break
		if len(lookup[j])==0:
			prefix.append(m[0])
		else:
			res=''
			for i in range(len(lookup[j])):
				temp=os.path.commonprefix([m,lookup[j][i]])
				if len(temp)==len(m):
					print -1
					return
				if len(temp)>len(res):
					res=temp
			prefix.append(m[:len(res)+1])
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
		
t=1
r12=0
for i in range(t):
	n=raw_input()
	n=int(n)
	blocked=[]
	unblocked=[]
	for m in range(n):
		x=raw_input()
		if x[0]=="-":
			blocked.append(x[2:])
		else:
			unblocked.append(x[2:])
	
	if len(blocked)==0:
		print 0
	else:
		trieutil(blocked,unblocked)
