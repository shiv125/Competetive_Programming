def fun(n):
	temp=n
	res=0
	res+=10*(temp%10)
	temp=temp/10
	res+=temp
	return res
s=raw_input()
hours=int(s[0:2])
mins=int(s[3:])
rec_mins=0
rec_hours=0
temp=hours
rec_hours=10*(temp%10)
temp=temp/10
rec_hours+=temp



temp=mins
rec_mins=10*(temp%10)
temp=temp/10
rec_mins+=temp
if hours==23 and mins>32:
	print 60-mins
elif hours%10>=6:
	if hours<=20 and hours>=10:
		print 20*60+2-(mins+hours*60)
	else:
		print 10*60+1-(mins+hours*60)
elif hours%10==5 and mins>rec_hours:
	if hours==5:
		print 10*60+1-(mins+hours*60)
	else:
		print 20*60+2-(mins+hours*60)
else:
	if mins<=rec_hours:
		print rec_hours-mins
	else:
		print 60+fun(hours+1)-mins



