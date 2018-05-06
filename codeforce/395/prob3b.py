n=input()
graph={}
for i in range(n):
	graph[i]=[]
for i in range(n-1):
	u,v=map(int,raw_input().split(" "))
	u=u-1
	v=v-1
	graph[u].append(v)
	graph[v].append(u)
color=map(int,raw_input().split(" "))
lookup=[0]*n
for i in graph:
	for j in graph[i]:
		if (color[i]!=color[j]):
			lookup[i]+=1
count=0
countx=0
t=0
for m in lookup:
	if m>=2:
		count+=1
	if m==1:
		countx+=1
if count>=2:
	print "NO"
	t=-1

else:
	if count==1:
		for i in range(len(lookup)):
			if lookup[i]>=2:
				print "YES"
				print i+1
				t=-1
				break
	else:
		
		if countx<=2:
			for i in range(len(lookup)):
				if (lookup[i]==1):
					t=-1
					print "YES"
					print i+1
					break

		if (countx==0 and t==0):
			print "YES"
			print 1
			
		elif (t==0 and countx>2):
			print "NO"
			
	


		


	
