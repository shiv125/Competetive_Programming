#def cout1s(s,i):
#	if 
s=raw_input()
i=len(s)-1
count=0
flag=0#even
while i>=0:
	if flag==0 and s[i]=='0':
		i-=1
	elif flag==1 and s[i]=='1':
		i-=1
		flag=1
	elif s[i]=='1' and flag==0:
		flag=1
		i-=1
		count+=1
	elif flag==1 and s[i]=='0':
		count+=1
		flag=0
		i-=1
print count
