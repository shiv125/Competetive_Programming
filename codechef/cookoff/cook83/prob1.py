t=input()
while t>0:
	t-=1
	s=raw_input()
	count1=0
	for i in range(len(s)-1):
		if s[i]=="D" and s[i+1]=="U":
			count1+=1
	if s[-1]=="D":
		count1+=1
	count2=0
	for i in range(len(s)-1):
		if s[i]=="U" and s[i+1]=="D":
			count2+=1
	if s[-1]=="U":
		count2+=1
	print min(count1,count2)
