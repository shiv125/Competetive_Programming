r,d=map(int,raw_input().split())
n=input()
e=10**(-9)
count=0
for i in range(n):
	x,y,ri=map(int,raw_input().split())
	if ((x*x+y*y)>=(r-d+ri)*(r-d+ri)) and ((x*x+y*y)<=(r-ri)*(r-ri)):
		count+=1
print count
