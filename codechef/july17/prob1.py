t=input()
while t>0:
	t-=1
	arr=map(str,raw_input().split())
	ln=len(arr)
	if ln==1:
		print arr[0][0].capitalize()+arr[0][1:].lower()
	elif ln==2:
		print arr[0][0].capitalize()+". "+arr[1][0].capitalize()+arr[1][1:].lower()
	else:
		print arr[0][0].capitalize()+". "+arr[1][0].capitalize()+". "+arr[2][0].capitalize()+arr[2][1:].lower()

		
