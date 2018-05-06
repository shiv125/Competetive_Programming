import sys
sys.setrecursionlimit(6000)
lookup={}
def fun(l):
	if l in lookup:
		return lookup[l]
	if l>=2:
		elem=10*s[l-2]+s[l-1]
		if elem<=26:
			if l==2:
				if elem==10 or elem==20:
					lookup[l]=1
				else:
					lookup[l]=2
			else:
				if elem==10 or elem==20:
					lookup[l]=fun(l-2)
				elif elem<10:
					lookup[l]=fun(l-1)
				else:
					lookup[l]=fun(l-1)+fun(l-2)
		else:	
			lookup[l]=fun(l-1)
	else:
		lookup[l]=1
	return lookup[l]
result=[]
while True:
	temp=raw_input()
	s=[]
	if temp=='0':
		break
	l=len(temp)
	for i in range(len(temp)):
		s.append(int(temp[i]))
	lookup={}
	res=fun(l)
	res=(res + 2**63) % 2**64 - 2**63
	result.append(res)
for i in result:
	print i

