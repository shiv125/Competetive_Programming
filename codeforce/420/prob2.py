def formula(x,y):
	return (x*(x+1))/2+((x+1)*y*(y+1))/2+(x*(x+1)*y)/2
m,b=map(int,raw_input().split())
ma=-1
for y in range(b+1):
	x=(b-y)*m
	ma=max(ma,formula(x,y))
print ma




