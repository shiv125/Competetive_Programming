def final(pop_arr, infected):
    index = None
    maxvalue = float('-inf')
    for (i,v) in enumerate(pop_arr):
        if i in infected: continue
        if v > maxvalue:
            maxvalue = v
            index = i
    return index
def code(Graph,m):
	j=1
	for r in Graph[i]:
		if (j==r):
			j+=1
		else:
			return j
	return j;	
t=input()
resultant=[]
for i in range(t):
	n=input()
	output=[0]*n
	Graph={}
	Hash={}
	Hash2={}
	pop_array=map(int,raw_input().split(' '))
	pop=[]
	for i in range(len(pop_array)):
		pop.append([i,pop_array[i]]);
	#print pop
	pop.sort(key=lambda x: x[1], reverse=True)
	c=1
	for i in pop:
		Hash[i[0]]=c
		Hash2[c]=i[0]
		c+=1
	#print Hash
	#print Hash2
	for i in range(n):
		Graph[i]=[Hash[i]]
	for i in range(n-1):
		v,u=map(int,raw_input().split(' '))
		Graph[v-1].append(Hash[u-1])
		Graph[u-1].append(Hash[v-1])
	
	for i in range(n):
		Graph[i]=sorted(Graph[i])
		#print Graph[i]
	#sorted(pop_array)
	#for i,v in enumerate(pop_array):
	
	for i in range(n):
		r=code(Graph,i)
		if (r==n+1):
			r=-1
		else:
			r=Hash2[r]
				
	#for i in range(n):
	#	max_=0
	#	r=-1
	#	for j in Graph[i]:
	#		if (pop_array[j]>max_):
	#			max_=pop_array[j]
	#			r=j
			
		#Graph[i].append(i)
		#r=final(pop_array,Graph[i])
		#if (r==None):
		#r=-1
		output[i]=str(r+1)
			
	resultant+=	[output]

for i in resultant:
	print " ".join(i)
	
		

