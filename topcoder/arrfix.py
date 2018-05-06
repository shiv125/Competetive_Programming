#convert A to B
class Arrfix:
	def mindiff(self,A,B,F):
		n=len(A)
		dist=0
		for i in range(n):
			if A[i]!=B[i]:
				if B[i] in F:
					F.remove(B[i])
				else:
					dist+=1
		for i in range(n):
			if A[i] in F:
				F.remove(A[i])
		dist+=len(F)
		return dist
a=Arrfix()
print a.mindiff(A,B,F)
