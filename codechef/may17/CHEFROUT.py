def temp(x):
	store=x[0]
	for i in range(1,len(x)):
		if x[i]=="C":
			if store=="E" or store=="S":
				return 'no'
		elif x[i]=="E" and store=="S":
			return 'no'
		store=x[i]
	return 'yes'
t=input()
for i in range(t):
	x=raw_input()
	print temp(x)
		
