win=[0]*4
#barc,malaga,realmad,eibar
teams=['Barcelona','Malaga','RealMadrid','Eibar']
t=input()
for i in range(t):
	team=[]
	goals=[]
	team1,goal1=map(str,raw_input().split())
	team2,goal2=map(str,raw_input().split())
	team3,goal3=map(str,raw_input().split())
	team4,goal4=map(str,raw_input().split())
	team.append(team1)
	team.append(team2)
	team.append(team3)
	team.append(team4)
	goal1=int(goal1)
	goal2=int(goal2)
	goal3=int(goal3)
	goal4=int(goal4)
	goals.append(goal1)
	goals.append(goal2)
	goals.append(goal3)
	goals.append(goal4)
	for j in range(4):
		if team[j]=='Barcelona':
			g1=goals[j]
	for j in range(4):
		if team[j]=='Eibar':
			g2=goals[j]
	for j in range(4):
		if team[j]=='RealMadrid':
			g3=goals[j]
	for j in range(4):
		if team[j]=='Malaga':
			g4=goals[j]
	flag=0
	if g3<g4:
		if g1>g2:
			flag=1
	if flag==0:
		print "RealMadrid"
	else:
		print "Barcelona"

			
