s1=raw_input()
s2=raw_input()
s3=raw_input()
res=''
dic={}
digits='0123456789'
for i in range(26):
	dic[s1[i]]=s2[i]
for i in s3:
	if i in digits:
		res+=i
	else:
		temp=i.lower()
		if temp==i:
			res+=dic[temp]
		else:
			res+=dic[temp].upper()
print res
