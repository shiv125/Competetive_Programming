#dp=[[[100000000 for x in range(11)] for y in range(11)] for z in range(11)]
#for a in range(10):
#	for b in range(10):
#		for c in range(10):
#			dp[a][b][c]=9999999
out=open("output_correct.txt","r+")
def fun(x,y,z):
	#dp[1][1][1]=3
	if x==0 and y==0 and z==0:
		return 0
	if x<0 or y<0 or z<0:
		return 10000000
	if dp[x][y][z]>1000000:
		dp[x][y][z]=min(min(fun(x-1,y,z)+a,fun(x,y,z-1)+a,fun(x,y-1,z)+a),min(fun(x-1,y-1,z)+b,fun(x,y-1,z-1)+b,fun(x-1,y,z-1)+b),fun(x-1,y-1,z-1)+c)
	return dp[x][y][z]
t=input()
while t>0:
	t-=1
	X,Y,Z,a,b,c=map(int,raw_input().split())
	x=min(X,Y,Z)
	lis=sorted([X,Y,Z])
	dp=[[[100000000 for x in range(Z+1)] for y in range(Y+1)] for z in range(X+1)]
	fun(X,Y,Z)
	#print dp[X][Y][Z]
	out.write(str(dp[X][Y][Z])+"\n")

