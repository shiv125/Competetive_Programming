def quicksum(numbers,total,count):
	if total==0 and len(numbers)==0:
		return count
	elif (len(numbers)==0 and total!=0):
		return 10000
	else:
		total1=total
		count1=count
		if len(numbers)==1:
			if numbers[0]==0:
				numbers.pop(0)
				count1+=1
				return count1
		if len(numbers)>0:
			total1=total-numbers[0]
			count1=count+1
			total2=total
			count2=0
		if len(numbers)>2:
			total2=total-(10*numbers[0]+numbers[1])
			count2=count+1
		else:
			total2=total1
			count2=count1
		if len(numbers)>2:
			return min(quicksum(numbers[1:],total1,count1),quicksum(numbers[2:],total2,count2))
		else:
			return min(quicksum(numbers[1:],total1,count1))
#numbers=[3,8,2,8,3,4]
x="1110"
numbers=[]
for i in x:
	numbers.append(int(i))
c=0
for j in range(len(numbers)):
	temp=len(numbers)
	if j>=temp:
		break
	else:
		if numbers[j]==0:
			c+=1
		else:
			c=0
		if c>1:
			t=j
			while c>0:
				numbers.pop(t)
				print numbers
				c-=1
				t-=1

print numbers
total=3
count=0
res=quicksum(numbers,total,count) -1
if res>900:
	print -1
else: 
	print res




