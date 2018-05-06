a=[]
while True:
	t=raw_input()
	if t=="":
		break
	else:
		t=map(int,t.split(" "))
		t.pop()
		curr_max_prod=t[0]
		max_prod=t[0]
		curr_min_prod=t[0]
		min_prod=t[0]
		zero=-1
		for i in range(1,len(t)):
			if t[i]==0:
				zero=1
			curr_max_prod=max(curr_max_prod*t[i],t[i])
			
			if curr_min_prod<0:
				if t[i]<0:
					curr_max_prod=max(curr_min_prod*t[i],curr_max_prod)
			curr_min_prod=min(curr_min_prod*t[i],t[i])

			if max_prod<curr_max_prod:
				max_prod=curr_max_prod
		if max_prod<0:
			if zero==1:
				max_prod=0
			
		a.append(max_prod)

for i in a:
	print i
