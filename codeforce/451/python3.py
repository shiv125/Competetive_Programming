n=input()
look={}
for i in range(n):
	z=raw_input().split()
	if z[0] in look:
		for j in range(len(z[2:])):
			look[z[0]].append(z[2+j])
	else:
		look[z[0]]=z[2:]
for i in look:
	temp=look[i]
	temp=list(set(look[i]))
	look[i]=temp
suffix={}
m=len(look)
for j in look:
	suffix[j]=[0]*len(look[j])
for j in look:
	for k in range(len(look[j])):
		suffix[j][k]=1
#print look
for i in look:
	for j in range(len(look[i])):
		for k in range(len(look[i])):
			if j!=k:
				if look[i][j].endswith(look[i][k]):
					suffix[i][k]=0
print m
#c=0
for i in look:
	print i,
	print sum(suffix[i]),
	for j in range(len(look[i])):
		if suffix[i][j]!=0:
			print look[i][j],
	print
