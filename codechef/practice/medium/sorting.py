import sys
comp_count=0
#def concatenate(a,pivot,b):
sys.setrecursionlimit(1500)
def sort(A):
	global comp_count
	less=[]
	greater=[]
	if len(A)<=1:
		return A
	pivot=A[(len(A)+1)/2-1]
	for i in range(len(A)):
		comp_count+=1
		if A[i]<pivot:
			less.append(A[i])
		elif A[i]>pivot:
			greater.append(A[i])
	return sort(less)+[pivot]+sort(greater)

#myout=open("output.txt","a")
#with open('testcases.txt',"r") as f:
#	inp=[]
#	for line in f:
#		inp.append(line)

n=input()
#n=int(inp[0])
arr=map(int,raw_input().split())
sort(arr)
print comp_count
