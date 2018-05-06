#8 Queen Problem
row=[0]*8
def place(r,c):	
	for prev in range(0,c):#check previously placed queen
		if row[prev]==r or abs(row[prev]-r)==abs(c-prev):
			return False
	return True
def backtrack(c):
	if c==8 and row[0]==0:
		for j in range(8):
			print j, row[j]+1
	for r in range(8):
		if place(r,c):
			row[c]=r
			backtrack(c+1)
backtrack(0)
		
