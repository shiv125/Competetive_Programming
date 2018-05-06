#from collections import deque
#import Queue
class Que():
	def __init__(self,queue=None):
		if queue is None:
			self.queue=[]
		else:
			self.queue=list(queue)
	def empt(self):
		if len(self.queue)==0:
			return 1
		return 0
	def get(self):
		return self.queue.pop(0)
	def put(self,element):
		self.queue.append(element)
		'''
class Que():
    def __init__(self, queue=None):
        if queue is None:
            self.queue = []
        else:
            self.queue = list(queue)
    def get(self):
        return self.queue.pop(0)
	def empt(self):
		if len(self.queue)==0:
			return True
		return False
    def put(self, element):
        self.queue.append(element)
	'''
def check(x,y):
	if x<0 or y<0 or x==n or y==m:
		return False
	if arr[x][y]==max_:
		return False
	return True
t=int(input())
result=[]
ax=[1,0,-1,0,1,1,-1,-1]
ay=[0,1,0,-1,1,-1,1,-1]
for i in range(t):
	n,m=map(int,raw_input().split())
	arr=[]
	max_=0
	for j in range(n):
		tt=map(int,raw_input().split())
		arr.append(tt)
		max_=max(max(tt),max_)
#	max_=0
#	for j in range(n):
#		max_=max(max(arr[j]),max_)
	total=0
	lookup=Que()
	for j in range(n):
		for k in range(m):
			if arr[j][k]==max_:
				lookup.put([j,k])
	lookup.put([-1,-1])
	#print lookup
	#print lookup.empt()
	while not lookup.empt():
		temp=0
		#x1,y1=lookup.get()
		while True:
			#x1=lookup[0][0]
			#y1=lookup[0][1]
			x1,y1=lookup.get()
			if x1==-1:
				break
			for p in range(8):
				new_x1=x1+ax[p]
				new_y1=y1+ay[p]
				if (check(new_x1,new_y1)==True):
					arr[new_x1][new_y1]=max_
					if temp==0:
						total+=1
						temp=1
					lookup.put([new_x1,new_y1])
		#lookup.get()
		if not lookup.empt():
			lookup.put([-1,-1])
	result.append(total)
for i in result:
	print i
