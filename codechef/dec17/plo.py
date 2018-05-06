import matplotlib.pyplot as plt


xr=[]
yr=[]
xb=[]
yb=[]
n,m=map(int,raw_input().split())
#m=6
for i in range(n):
	a,b=map(int,raw_input().split())
	xr.append(a)
	yr.append(b)
for i in range(m):
	a,b=map(int,raw_input().split())
	xb.append(a)
	yb.append(b)
plt.plot(xr, yr, 'ro',xb,yb,'bo')
#plt.axis([0, 6, 0, 20])
plt.show()

