class DivFreed2:
	def count(n,k):
		mod=1000000007
		#let f[t][i] represents no. of arrays of length t and they starts 
		#element i
		#f[t][i]=f[t-1][j] if j doesn't divide i
		f=[[0 for x in range(t+1)] for y in range(k+1)]
		divisors={}
		for i in range(1,k+1):
			divisors[i]=[]
		#seive
		for i in range(1,k+1):
			for j in range(2*i,k+1,i):
				divisors[j].append(i)
		#sum over all f[t-1][j] and subtract divisors from it
		for i in range(1,k+1):
			f[1][i]=1
		for t in range(2,n+1):
			for i in range(1,k+1):
				sum_+=f[t-1][i]
			sum_=sum_%mod
			for i in range(1,k+1):
				f[t][i]=sum_
				for j in divisors[i]:
					f[t][i]=(f[t][i]-f[t-1][j])%mod
		total=0
		for i in range(1,k+1):
			total+=f[n][i]
			total%=mod
		total%=mod
		return total

