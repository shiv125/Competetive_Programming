#brute force to testing
#t=int(input())
inp=open("input.txt","r+")
out=open("output_correct.txt","r+")
import random
t=random.randint(50,90)
result=[]
inp.write(str(t)+"\n")
for i in range(t):
	#n=int(input())
	n=random.randint(2,100)
	count =0
	#n=12
	#arr=map(int,raw_input().split())
	arr=[0]*n
	
	for i in range(2*n/3):
		arr[random.randint(0,n-1)]=1
	#my test case
	#arr=[0,0,1,1,1,1,0,1,0,0,0,1]
	k=" ".join(str(x) for x in arr)
	inp.write(str(n)+"\n")
	inp.write(k+"\n")

	c1=0
	i=0
	while True:
		c1=0
		i=0
		while i<n-1:
			if arr[i]==0 and arr[i+1]==1:
				arr[i]=1
				arr[i+1]=0
				i+=2
			else:
				c1+=1
				i+=1
		if c1==n-1:
			break
		count+=1
	result.append(count)
for i in result:
	out.write(str(i)+"\n")
