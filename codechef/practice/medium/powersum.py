def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

def combination(m,k):
    if k <= m:
        return factorial(m)/(factorial(k) * factorial(m - k))
    else:
        return 0
def ncr(n,r):
    rs=1
    for i in range(0,min(r,n-r)):
    	rs=(rs*(n-i))/(i+1)
    return rs
def Bernoulli(m):
    if m == 0:
        return 1
    else:
        t = 0
        for k in range(0, m):
            t += ncr(m, k) * Bernoulli(k) / (m - k + 1)
        return 1 - t
br=[0]*102

ans=0
for i in range(1):
	br[i]=Bernoulli(100)
print "e"
'''
for i in range(k):
	if i%2==0:
		ans+=combination(k+1,i)*br[j]*n**(k+1-j)
	ans=int(ans/(k+1))
print ans%p

'''
