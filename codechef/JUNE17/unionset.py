t=input()
while t>0:
	t-=1
	N,K=map(int,raw_input().split())
	#lookup=[[0 for x in range(K)] for y in range(N)]
	all_list=[]
	lookup=[False]*(K+1)
	for i in range(N):
		arr=map(int,raw_input().split())
		#min_=min(min_,arr[0])
		all_list.append(arr)
	total=0
	for i in range(N):
		count1=0
		for m in range(all_list[i][0]):
			lookup[all_list[i][m+1]]=True
		count1=all_list[i][0]
		count2=0
		for j in range(i+1,N):
			count2=0
			if count1+all_list[j][0]>=K:
				for m in range(all_list[j][0]):
					if lookup[all_list[j][m+1]]==False:
						count2+=1
				if count1+count2==K:
					total+=1
		for m in range(all_list[i][0]):
			lookup[all_list[i][m+1]]=False
	print total	
