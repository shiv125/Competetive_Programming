n,m=map(int,raw_input().split())
s=raw_input()
t=raw_input()
ma=1000000
ind=-1
for i in range(m-n+1):
	count=0
	for j in range(n):
		if s[j]!=t[j+i]:
			count+=1
	if ma>count:
		ind=i
	ma=min(ma,count)
print ma
for j in range(n):
	if s[j]!=t[ind+j]:
		print j+1,
