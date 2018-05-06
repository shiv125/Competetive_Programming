n=input()
count=0
flag=False
orde=True
for i in range(2*n):
	inp=raw_input()
	if inp[0]=='a':
		flag=True
		com,val=map(str,inp.split())
		val=int(val)
		if i==0:
			top=val
		else:
			if val!=top-1:
				orde=False
			top=val
	else:
		if orde==False and flag==True:
			count+=1
		flag=False
		orde=True
print count
			
