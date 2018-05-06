def binarysearch(elem,s,ind,low,high):
	if low>high:
		return -1
	mid=(low+high)/2
	val1=int(s[ind+1:mid+1])
	val2=elem
	val3=int(s[mid+1:])
	if val1+val2==val3:
		return mid+1
	elif val1+val2<val3:
		low=mid+1
	else:
		high=mid-1
	return binarysearch(elem,s,ind,low,high)

def fun(s):
	first=''
	flag=0
	store=-2
	for ind in range(len(s)):
		first=first+s[ind]
		first1=int(first)
		store=max(store,binarysearch(first1,s,ind,ind+1,len(s)-1))
		if store!=-1:
			break
	if store==-1:
		print -1
	else:
		print s[:ind+1]+'+'+s[ind+1:store]+'='+s[store:]

s=raw_input()
fun(s)
