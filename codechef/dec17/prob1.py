t=input()
while t>0:
	t-=1
	n,m=map(int,raw_input().split())
	mat=[0]*n
	cost1=0#R
	cost2=0#G
	for i in range(n):
		mat[i]=list(raw_input())
	
	for i in range(n):
		for j in range(m):
			if i%2==0:
				if j%2==0:
					if mat[i][j]=='G':
						cost1+=3
				else:
					if mat[i][j]=='R':
						cost1+=5
			else:
				if j%2!=0:
					if mat[i][j]=='G':
						cost1+=3
				else:
					if mat[i][j]=='R':
						cost1+=5
	for i in range(n):
		for j in range(m):
			if i%2!=0:
				if j%2==0:
					if mat[i][j]=='G':
						cost2+=3
				else:
					if mat[i][j]=='R':
						cost2+=5
			else:
				if j%2!=0:
					if mat[i][j]=='G':
						cost2+=3
				else:
					if mat[i][j]=='R':
						cost2+=5
	print min(cost1,cost2)
