MAX=10**4+1
first_dp=[0]*MAX
second_dp=[0]*MAX
result=[]
while True:
	first=map(int,raw_input().split())
	if first[0]==0:
		break
	else:
		second=map(int,raw_input().split())
		first=first[1:]
		second=second[1:]
		store_first=[]
		store_second=[]
		n1=len(first)
		n2=len(second)#n1 is max
		first_dp[0]=first[0]
		second_dp[0]=second[0]
		total=0

		for i in range(1,n1):
			first_dp[i]=first_dp[i-1]+first[i]
		for i in range(1,n2):
			second_dp[i]=second_dp[i-1]+second[i]
		count={}
		for i in range(n1):
			count[first[i]]=i
		for i in range(n2):
			if second[i] in count:
				store_first.append(count[second[i]])
				store_second.append(i)

		if len(store_first)==0:
			ma=max(first_dp[n1-1],second_dp[n2-1])
		else:
			for i in range(len(store_first)):
				if i==0:
					temp1=first_dp[store_first[0]]
				else:
					#if store_first[i-1]!=0:
					temp1=first_dp[store_first[i]]-first_dp[store_first[i-1]]
					#else:
					#	temp1=first_dp[store_first[i]]
				if i==0:
					temp2=second_dp[store_second[0]]
				else:
					#if store_second[i-1]!=0:
					temp2=second_dp[store_second[i]]-second_dp[store_second[i-1]]
					#else:
					#	temp2=second_dp[store_second[i]]
				total+=max(temp1,temp2)
			c1=store_first[-1]
			c2=store_second[-1]
			temp1=first_dp[n1-1]-first_dp[c1]
			temp2=second_dp[n2-1]-second_dp[c2]
			total+=max(temp1,temp2)
			ma=total
		result.append(ma)
for i in result:
	print i
