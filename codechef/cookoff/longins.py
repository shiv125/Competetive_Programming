#longest increasing subsequence, given a array find the longest subsequence in the sorted order 
#my algo works in O(n^2) but O(nlogn) is also possible
input_=[10,22,9,33,21,50,41,60,80]
n=len(input_)
LongInSub=[1]*n
for i in range(1,n):
	for j in range(i):
		if (input_[j]<input_[i]):
			LongInSub[i]=max(1+LongInSub[j],LongInSub[i])
print LongInSub
length=max(LongInSub)
print length
