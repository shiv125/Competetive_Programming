#count distinct

t=input()
for m in range(t):
	N=input()
	arr=map(int,raw_input().split())
	print N-max(arr)	
	
