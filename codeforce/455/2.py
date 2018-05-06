from munkres import Munkres,print_matrix
t=input()
while t>0:
	t-=1
	n,m=map(int,raw_input().split())
	mat=[[10000000 for x in range(n)] for y in range(n)]
	for i in range(n):
		arr=map(int,raw_input().split())
		for j in range(m):
			mat[i][j]=arr[j]
	mi=Munkres()
	indexes = mi.compute(mat)
	#print_matrix(mat, msg='Lowest cost through this matrix:')
	total = 0
	for row,col in indexes:
		if col<=m-1:
			total+=mat[row][col]
	print total
