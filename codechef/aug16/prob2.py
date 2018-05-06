t=input()
result=[]
while t>0:
	t-=1
	n=input()
	arr=map(int,raw_input().split())
	count=0
	visited=[0]*n
	ans=0
	for i in range(n):
		if visited[i]==0:
			count+=1
			visited[i]=count
			j=(i+arr[i]+1)%n
			while visited[j]==0:
				visited[j]=count
				j=(j+arr[j]+1)%n
			if visited[j]==count:
				ans+=1
				k=(j+arr[j]+1)%n
				while k!=j:
					ans+=1
					k=(k+arr[k]+1)%n
	print ans








		
