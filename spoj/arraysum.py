import heapq
from sortedcontainers import SortedList, SortedSet, SortedDict
heapsize=0
def parent(A,i):
	if i==0:
		return
	else:
		return i/2
def left(A,i):
	global heapsize
	if 2*i<=heapsize:
		return 2*i
	else:
		return
def right(A,i):
	global heapsize
	if 2*i+1<=heapsize:
		return 2*i+1
	else:
		return

def maxheapify(A,i):
	global heapsize
	l=left(A,i)
	r=right(A,i)
	#print l,r
	#print heapsize
	if l==None or r==None:
		return
	if l<heapsize and A[l]>A[i]:
		large=l
	else:
		large=i
	if r<heapsize and A[r]<A[large]:
		large=r
	if large!=i:
		#swap(A[i],A[large])
		temp=A[i]
		A[i]=A[large]
		A[large]=temp
		maxheapify(A,large)
def buildheap(A):
	global heapsize
	heapsize=len(A)
	for i in range(len(A)/2,-1,-1):
		maxheapify(A,i)
def insert(A,key):
	global heapsize
	heapsize+=1
	A[heapsize-1]=-1
	increasekey(A,heapsize-1,key)
def extrmax(A):
	global heapsize
	ma=A[0]
	A[0]=A[heapsize-1]
	heapsize-=1
	maxheapify(A,0)
	return ma
def increasekey(A,i,key):
	if key<A[i]:
		return
	A[i]=key
	while i>0 and A[parent(A,i)]<A[i]:
		temp=A[i]
		A[i]=A[parent(A,i)]
		A[parent(A,i)]=temp
		i=parent(A,i)
n=input()
arr=map(int,raw_input().split())
k=input()
ma=arr[0]
res=[]
heap=[]
heapsize=0
for i in range(k):
	#heapq._heappush_max(hpma,arr[i])
	heap.append(arr[i])
	ma=max(ma,arr[i])
buildheap(heap)
res.append(ma)
#print heap
for i in range(k,n):
	print heap
	extrmax(heap)
	insert(heap,arr[i])
	print heap
	#heap.add(arr[i])
	ma=extrmax(heap)
	res.append(ma)
		
print res
