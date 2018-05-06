import string
out=open("output4.txt","a")
t=input()
for s in range(t):
	list1=[]
	list0=[]
	N=input()
	for q in range(N):
		list0.append(raw_input())
	for j in range(N):
		list1.append("".join(list0[j].split()))
	max_=0
	t=string.ascii_uppercase
	H={}
	indexarray=[]
	for i in range(N):
		for m in t:
			H[m]=0
		for j in list1[i]:
			H[j]=1
		total=0
		for k in H:
			total+=H[k]
		if (max_<total):
			max_=total
			index=i
	comp=list('zzzzzzzzzzzzzzzzzzzzz')
	for i in range(N):
		for m in t:
			H[m]=0
		for j in list1[i]:
			H[j]=1
		total=0
		for k in H:
			total+=H[k]
		if (max_==total):
			
			if (comp>list(list0[i])):
				comp=list(list0[i])

				index=i
	
	out.write("Case #"+str(s+1)+": "+list0[index]+"\n")
