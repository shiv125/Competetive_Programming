def mp():
	return map(int,raw_input().split())
s=raw_input()
z='aeiou'
c=0
d='13579'
for i in s:
	if i in z or i in d:
		c+=1

print c
