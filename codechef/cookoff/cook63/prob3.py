def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

test=input()
while test>0:
	test-=1
	ln=input()
	arr=map(str,raw_input().split())
	if len(arr)==1:
		print arr[0]
	else:
		t= long_substr(arr)
		n=len(t)
		mi=30
		elem=''
		ind=-1
		for i in range(len(arr)):
			if mi>len(arr[i]):
				mi=len(arr[i])
				elem=arr[i]
				ind=i
		arr.pop(ind)
		res=t
		for i in range(mi-n+1):
			t=elem[i:i+n]
			arr.append(t)
			s=long_substr(arr)
			if len(s)==n:
				if s<res:
					res=s
			arr.pop()
		print res
