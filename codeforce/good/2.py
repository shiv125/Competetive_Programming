def mp():
	return map(int,raw_input().split())

n,m=mp()
mat=[]
z=[]
for i in range(n):
	mat.append(list(raw_input()))
mapi=raw_input()



z=['0123', '0132', '0213', '0231', '0321', '0312', '1023', '1032', '1203', '1230', '1320', '1302', '2103', '2130', '2013', '2031', '2301', '2310', '3120', '3102', '3210', '3201', '3021', '3012']
for i in range(24):
	z[i]=list(z[i])
	
c=0
si,sj=-1,-1
ei,ej=-1,-1

for i in range(n):
	for j in range(m):
		if mat[i][j]=="S":
			si,sj=i,j
		if mat[i][j]=="E":
			ei,ej=i,j
li,lj=si,sj
#print si,sj,ei,ej,li,lj
for k in z:
	si,sj=li,lj
	#print si,sj
	for i in mapi:
		if si<0 or sj<0:
			break
		if si>n-1 or sj>m-1:
			break
		if mat[si][sj]=='#':
			break
		if mat[si][sj]=="E":
			break
		if i==k[0]:
			sj-=1
			
		if i==k[1]:
			si-=1
			#print 's'
		if i==k[2]:
			sj+=1
		if i==k[3]:
			si+=1
	
	if si==ei and sj==ej:
		c+=1
	
print c
	
