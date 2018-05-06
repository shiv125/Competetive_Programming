import sys
test=input()
alpha='abcdefghijklmnopqrstuvwxyz'
result=[]
for i in range(test):
	lookup=[0]*26
	w,k=map(str,raw_input().split())
	k=int(k)
	ln=len(w)
	for m in w:
		for j in range(26):
			if m==alpha[j]:
				lookup[j]+=1	
	lookup.sort()
	tot=lookup[-1]
	f=10**6
	for j in lookup:
		flag=0
		total=0
		for p in range(26):
			if lookup[p]<j and lookup[p]>0:
				total+=lookup[p]
				#flag=1
			elif lookup[p]>j+k and lookup[p]>0:
				total+=lookup[p]-(j+k)
				#flag=1
		if f>total:
			f=total
		#if flag==0:
		#	F[j]=10**6
	result.append(f)
for i in result:
	print i
sys.exit()
