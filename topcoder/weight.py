class DoubleWeights:
	def minimalCost(self,a,b):
		n=len(a)
		g1={}
		for i in range(n):
			g1[i]=[]
		g2={}
		for i in range(n):
			g2[i]=[]
		for i in range(n):
			for j in range(n):
				if a[i][j]!='.':
					g1[i].append(j)
		x=BFS(g1,0,1,path_queue)
		print x
		if (x==[]):
			return -1
		else:
			opt=[]
			for i in x:
				w1=0
				w2=0
				for j in range(1,len(i)):
					w1+=int(a[i[j-1]][i[j]])
					w2+=int(b[i[j-1]][i[j]])
				opt.append(w1*w2)
			return min(opt)
				
class MyQUEUE: # just an implementation of a queue
	
	def __init__(self):
		self.holder = []
		
	def enqueue(self,val):
		self.holder.append(val)
		
	def dequeue(self):
		val = None
		try:
			val = self.holder[0]
			if len(self.holder) == 1:
				self.holder = []
			else:
				self.holder = self.holder[1:]	
		except:
			pass
			
		return val	
		
	def IsEmpty(self):
		result = False
		if len(self.holder) == 0:
			result = True
		return result


path_queue = MyQUEUE() # now we make a queue


def BFS(graph,start,end,q):
	result=[]
	temp_path = [start]
	
	q.enqueue(temp_path)
	
	while q.IsEmpty() == False:
		tmp_path = q.dequeue()
		last_node = tmp_path[len(tmp_path)-1]
		if last_node == end:
			result.append(tmp_path)
		for link_node in graph[last_node]:
			if link_node not in tmp_path:
				new_path = []
				new_path = tmp_path + [link_node]
				q.enqueue(new_path)
	return result
'''
a=["..14","..94", "19..",
 "44.."]
b=["..94",
 "..14",
 "91..",
 "44.."]
 
p=DoubleWeights()
print p.minimalCost(a,b)
'''
