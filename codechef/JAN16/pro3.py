t=input()
while t>0:
	t-=1
	n,m=map(int,raw_input().split())
	mat=[0]*n
	for i in range(n):
		mat[i]=raw_input()
	mi_row=n
	ma_row=0
	mi_col=m
	ma_col=0
	flag=0
	for i in range(n):
		for j in range(m):
			if mat[i][j]=='*':
				flag=1
				mi_row=min(i,mi_row)
				ma_row=max(i,ma_row)
				mi_col=min(j,mi_col)
				ma_col=max(j,ma_col)
	if flag==1:
		print (max(ma_col-mi_col+1,ma_row-mi_row+1))/2+1
	else:
		print 0

				

