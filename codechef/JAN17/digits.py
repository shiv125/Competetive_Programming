def gcd(a,b):
	if (b==0):
		return a;
	else:
		return gcd(b,a%b)
t=input()
for i in range(t):
	N=input()
	Str=raw_input()
	#S=map(int,raw_input().split())
	M,X,P=map(int,raw_input().split())
	k=3
	if (M==1):
		
		r=S[0]
		k=r
		for i in range(N):
			k=min(k,gcd(S[i],r))
		print k
	
	
	part=k+1
	#c=N/part
	c=2
	array=[]
	if (M==2):
		if (N%2==0):
			#part=N/M
			for j in range(0,N,2):
				array.append(Str[j:j+c])
				#return array
			#increase seperators
			#array1=[0]*(part+1)
			#for j in range(part+1):
			#	array1[j]=Str[j:j+1]
			print array
			array1=[]
			for y in range(part):
				array1=[]
				p=0
				for j in range(0,y,2):
					
					array1.append(Str[j:j+c])
					p+=1
				for m in range(y,y+2):
					array1.append(Str[m+p:m+1+p])
					#array1[m+1]=Str[m+1:m+2]

				#array1[0]=Str[0:1])
				#array1[1]=Str[1:2]
				
			#	arra1[0]=Str[0:2]
			#	array1[1]=Str[2:3]
			#	array1[2]=Str[3:4]

				for j in range(y+2,N,2):
				
					array1.append(Str[p+j:p+j+c])
					
					
				print array1
				#return array
				ab=1
				for m in range(y+1,6,2):
					array1[ab]=Str[m:m+c]
					array1[ab+1]=Str[m+c:m+c+1]
					ab+=1
					print array1
					#return array
			
	#		for j in range(3,part+1):
	#			
	#			array1[j]=Str[j:j+c]
				#return array
	#		for m in range(3,part+1):
	#			array1[m]=Str[m:m+c]
	#			array1[m+1]=Str[m+c:m+c+1]
				#return array

			
			#move seperator
			#array1[1]=Str[1:3]
			#array1[2]=Str[3:4]

			#array1[2]=Str[3:5]
			#array1[3]=Str[5:6]
			

			#similarly

		
