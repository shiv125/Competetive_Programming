with open('input.txt',"r") as f0:
	inp=[]
	for line in f0:
		inp.append(line)
inp=[x.strip() for x in inp]
with open('output_correct.txt',"r") as f:
	out=[]
	for line in f:
		out.append(line)
out=[x.strip() for x in out]
with open('myout.txt',"r") as f1:
	out1=[]
	for line in f1:
		out1.append(line)
out1=[x.strip() for x in out1]
stin=[]
for i in range(len(out)):
	if out[i]!=out1[i]:
		print inp[2*i+2]
		print "Your answer = "+str(out1[i])
		print "Correct answer = "+str(out[i])+"\n"

	
