def gcd(a,b):
	if (b==0):
		return a;
	else:
		return gcd(b,a%b)
#def gcd(a,b,c):
#	return gcd1(a,gcd1(b,c))
	

t=input()
N=input()
X=map(int,raw_input().split())
Y = [[0 for x in range(N)] for x in range(N)]
P=(X[0]*X[0])%359999
for i in range(N):
	for j in range(N):
		Y[i][j]=(X[i]*X[j])%359999
		#print Y[i][j]
#print Y
count=0
#for c in range(N):
#	for d in range(N):
#		if (gcd(k,Y[c][d])==1):
#			print 1
#for a in range(N):
#	for b in range(N):
#		for c in range(N):
#			for i in range(N):
#				for j in range(N):
#					for k in range(N):
#						if (gcd(Y[a][b],gcd(Y[c][i],Y[j][k]))==1):
					
#							count+=1

count2=0

for i in range(N):
	for j in range(N):
		for k in range(N):
			for a in range(N):
				if (gcd(Y[i][j],Y[k][j])==1):
					count2+=1
#print (N**2*count2)%10**9+7
print count2
#print count%(10**9+7)
