#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define rep(i,n) for (int i=1;i<=n;i++)
#define down(i,n) for (int i=n-1;i>-1;i--)
#define pb push_back
#define pll pair<int, int>
#define cities 100007
#define ma 1000007
#define IcF 10000000
using namespace std;
const ll INF = 1000000000000ll;
vector<pll> departure[ma],arrival[ma];
ll left_cost[ma],right_cost[ma];
ll curr_mi[cities];
int city,cost;
int main(){
f(i,ma){left_cost[i]=INF;right_cost[i]=INF;}
ll n,m,k;
int d,f,t,c;
cin>>n>>m>>k;
f(i,m){scanf("%d%d%d%d",&d,&f,&t,&c);if (f==0) arrival[d].pb({t,c});else departure[d].pb({f,c});}
ll mi=INF*n;
f(i,n+1) curr_mi[i]=INF;
f(i,ma){f(j,departure[i].size())
{city=departure[i][j].first;cost=departure[i][j].second;
if (curr_mi[city]>cost){mi=mi+cost-curr_mi[city];curr_mi[city]=cost;}
}
left_cost[i]=mi;}
f(i,n+1) curr_mi[i]=INF;
mi=INF*n;
//////
down(i,ma-1){f(j,arrival[i].size())
{city=arrival[i][j].first;cost=arrival[i][j].second;
if (curr_mi[city]>cost){mi=mi+cost-curr_mi[city];curr_mi[city]=cost;}
}
right_cost[i]=mi;}
mi=INF*n;
for (int i=1;i<ma-k;i++) {mi=min(mi,left_cost[i-1]+right_cost[i+k]);}
if (mi<INF)
	cout<<mi<<endl;
else
	cout<<-1<<endl;
return 0;}	
