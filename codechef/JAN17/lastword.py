#def lastword(S):
#	e=S.pop()
#	return lastword(S)
def lastword(S):
	res=[]
	if (len(S)==2):
		#res=[]
		res+=[[S[0]]+[S[1]]]
		res+=[[S[1]]+[S[0]]]
		return res
	else:
		e=S.pop()
		
		#rint S
		a=lastword(S)
		first=[]
		for i in a:
			first+=[i+[e]]
		last=[]
		for i in a:
			last+=[[e]+i]
		resi=[]
		resi=first+last	
		print resi
		return resi
		
S=['J','A','M','B']
lastword(S)
print lastword(S)
