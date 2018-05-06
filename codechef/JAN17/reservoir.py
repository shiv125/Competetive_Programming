def fun(input_,N,M):
		#for water
	for i in range(N):
		for j in range(M):
			if (input_[i][j]=='W'):
				if (j==0 or j==M-1):
					return 0
				elif (input_[i][j-1]!='B' or input_[i][j+1]!='B'):
					return 0
				elif (i==N-1):
					return 0
				elif (input_[i+1][j]=='A'):
					return 0
				elif (i!=0):
					if (input_[i-1][j]=='B'):
						return 0
			if (input_[i][j]=='B'):
				if (i!=N-1):
					if (input_[i+1][j]!='B'):
						return 0
			
	return 1
				
				

t=input()
result=[0]*t
for i in range(t):
	N,M=map(int,raw_input().split(' '))

	input_=[[0]*M]*N
	for j in range(N):
		input_[j]=raw_input()
	k=fun(input_,N,M)
	result[i]=k	
for i in result:
	if (i==1):
		print 'yes'
	else:
		print 'no'
		
