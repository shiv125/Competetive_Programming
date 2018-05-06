import string
import sys
#import psyco
#psyco.full()
#out=open("output.txt","a")
#t=input()
#print t
with open('large-file.txt') as the_file:
	q=0
	for line in the_file:
		if (q==1):
			A,B,N,K= map(int,line.split(" "))
			count=0
			print A,B,N,K
			temp=[]
			for i in range(1,K+1):	
				r=(i**A)%K
				temp.append(K-r)
				if (i**)
			for i in range(1,K+1):
				if (i**B=temp[i-1]):
					
							
			
					
count=1
						#count+=((N-i)/K+1)*((N-j)/K+1)
			print count
	#out.write("Case #"+str(m+1)+": "+str(count%(10**9+7))+"\n")

		q=1
#t=int(raw_input())
#for m in range(t):
#	A, B, N, K = [int(s) for s in raw_input().split(" ")]
	#A,B,N,K = raw_input().split()
	#A=int(A)
	#B=int(B)
	#N= int(N)
	#K=int(K)
	#x=map(int,raw_input().split(" "))
	#print x
	#A=x[0]
	#B=x[1]
	#N=x[2]
	#K=x[3]
#	count=0
#	for i in range(1,K+1):		
#		for j in range(1,K+1):
#			if (i!=j):
#				if ((i**A+j**B)%K==0):
#					count+=((N-i)/K+1)*((N-j)/K+1)
	#out.write("Case #"+str(m+1)+": "+str(count%(10**9+7))+"\n")
#	print count
