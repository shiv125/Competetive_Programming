n=input()
s=raw_input()
n1=2*n
res=''
count=[0]*4
l={}
d='ABCD'
l['A']=0
l['B']=1
l['C']=2
l['D']=3
for i in range(n1):
	count[l[s[i]]]+=1
res=''
for j in d:
	if j!=s[0]:
		if count[l[j]]<n:
			res+=j
			count[l[j]]+=1
			break
left=res[0]
for i in range(1,n1):
	ma=5
	for j in d:
		if j!=s[i] and j!=left:
			if count[l[j]]<n:
				if ma>count[l[j]]:
					ma=count[l[j]]
					r=j
	count[l[r]]+=1
	res+=r
	left=r
print res
