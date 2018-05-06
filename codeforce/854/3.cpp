#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define MAX 600003
#define MA 10000007
using namespace std;
vector<ll> look[MA];
int main(){
ll n,k,temp;cin>>n>>k;
ll res[n];
ll cost[n],cost1[n];
ll used[n+1];
f(i,n+1) {used[i]=0;}
f(i,n) cin>>cost[i];
f(i,n) cost1[i]=cost[i];
f(i,n) {temp=cost1[i];look[temp].push_back(i+1);}
priority_queue<ll> que;
for(int i=1;i<n+1;i++) que.push(i);
for(int i=1;i<MA;i++){
for(int j=look[i].size()-1;j>-1;j--){
	temp=look[i][j];
	que.top(
	while (1){
	if ((used[look[i][j]]==1) or look[i][j]<k+1){
		look[i][j]++;}
	else{ res[temp-1]=que.top();used[look[i][j]]=1;break;}
	}
	}}
ll tot=0;
f(i,n) {tot=tot+cost[i]*(res[i]-i-1);}
cout<<tot<<endl;
f(i,n) cout<<res[i]<<" ";

cout<<endl;
return 0;}
