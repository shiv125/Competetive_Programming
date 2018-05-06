t=raw_input()
#t='aBddulbasaurrgndgbualdBdsagaurrgndbb'
#S=t.split(' ')

x=['B','u','l','b','s','a','r']
H={}
for i in x:
	H[i]=0

for j in t:
	if (j in H):
		H[j]+=1
	#for i in range(len(x)):
	#	if j==x[i]:
	#		H[i]+=1
k=100000
H['a']=H['a']/2
H['u']=H['u']/2
for j in H:
	k=min(H[j],k)
#print H

print k
#for i in S:
	
