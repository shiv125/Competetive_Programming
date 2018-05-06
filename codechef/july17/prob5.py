t=input()
while t>0:
	t-=1
	n=input()
	tree={}
	tree2={}
	parent={}
	for i in range(1,n+1):
		tree[i]={}		
	# 1 is a root
	root=1
	for i in range(n-1):
		u,v,c=map(int,raw_input().split())		
		if u==1:
			parent[v]=[1,c]
		else:
			if u not in parent:
				parent[u]=[v,c]
				#tree[u][v]=c
			else:
				parent[v]=[u,c]
				#tree[v][u]=c
#	for i in range(1,n+1):
#		if i not in parent:
	#		root=i
	#		break
	
	m=input()
	for y in range(m):
		u,v,k1=map(int,raw_input().split())
		x=u
		path1=[u]
		while x!=root:
			x=parent[x][0]
			path1.append(x)
		x=v
		path2=[v]
		while x!=root:
			x=parent[x][0]
			path2.append(x)
		flag=0
		lca=root
		for j in range(len(path1)):
			for k in range(len(path2)):
				if path1[j]==path2[k]:
					flag=1
					lca=path1[j]
					break
			if flag:
				break
		res=0
		z=u
		flag=0
		#print path1
		#print path2
		#print parent
		#print k1
		if path1[0]!=lca:
			for i in range(1,len(path1)):
				#if flag:
				#	break
				if z==lca:	
					break
			#	temp1=z
			#	temp2=path1[i]
				#if parent[z]!=path1[i]:
				#	temp1=path1[i]
				#	temp2=z
				#print parent[z]
				if parent[z][1]<=k1:
					res^=parent[z][1]
				z=path1[i]
		z=v
		flag=0
		#print path1
		
		if path2[0]!=lca:
			for i in range(1,len(path2)):
				if z==lca:	
					break
				if parent[z][1]<=k1:
					l=parent[z][1]
					res^=l
				z=path2[i]
		print res
