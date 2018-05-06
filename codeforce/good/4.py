import math
n,r=map(int,raw_input().split())
z=4*r*r
def func(x1,y1,x2):
    if z-(x2-x1)**2<0:
        return r
    else:
        return math.sqrt((z-(x2-x1)**2)*1.0)+y1*1.0 
b=[r]
a=raw_input().split()
for i in range(1,n):
    ans=r
    for j in range(i):
        x1=float(a[j])
        y1=float(b[j])
        x2=float(a[i])
        #print x1,y1,x2
        ans=max(ans,func(x1,y1,x2))
        #print z
    b.append(ans)
for i in range(len(b)):
    print b[i],

