n,m=map(int,raw_input().split())
arr=[]
for i in range(n):
	arr.append(map(int,raw_input().split()))
rows=[0]*n
for i in range(n):
	rows[i]=min(arr[i])
res_rows=[]
res_cols=[]
if n<m:
	for i in range(n):
		if rows[i]>0:
			for j in range(rows[i]):
				res_rows.append(i+1)
			for j in range(m):
				arr[i][j]-=rows[i]
	cols=[1000]*m
	for i in range(m):
		for j in range(n):
			cols[i]=min(arr[j][i],cols[i])
	for i in range(m):
		if cols[i]>0:
			for j in range(cols[i]):
				res_cols.append(i+1)
			for j in range(n):
				arr[j][i]-=cols[i]
	flag=0
	for i in range(n):
		for j in range(m):
			if arr[i][j]!=0:
				flag=1
				break
	if flag:
		print -1
	else:
		print len(res_rows)+len(res_cols)
		for i in res_rows:
			print "row "+str(i)
		for i in res_cols:
			print "col "+str(i)
else:
	cols=[1000]*m
	for i in range(m):
		for j in range(n):
			cols[i]=min(arr[j][i],cols[i])
	for i in range(m):
		if cols[i]>0:
			for j in range(cols[i]):
				res_cols.append(i+1)
			for j in range(n):
				arr[j][i]-=cols[i]
	rows=[0]*n
	for i in range(n):
		rows[i]=min(arr[i])
	for i in range(n):
		if rows[i]>0:
			for j in range(rows[i]):
				res_rows.append(i+1)
			for j in range(m):
				arr[i][j]-=rows[i]

	flag=0
	for i in range(n):
		for j in range(m):
			if arr[i][j]!=0:
				flag=1
				break
	if flag:
		print -1
	else:
		print len(res_rows)+len(res_cols)
		for i in res_rows:
			print "row "+str(i)
		for i in res_cols:
			print "col "+str(i)

	
