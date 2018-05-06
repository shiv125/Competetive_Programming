#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
using namespace std;
int main(){
int n,m;
int black=0,size=0;
char c;
cin>>n>>m;
int mat[n][m];
f(i,n){
f(j,m){cin>>c; if (c=='W') mat[i][j]=0;else mat[i][j]=1;}}
int lp=m,rp=-1,up=n,dp=-1;
f(i,n){f(j,m){if (mat[i][j]==1){
black++;
up=min(up,i);dp=max(dp,i);lp=min(lp,j);rp=max(rp,j);
}}}
size=max(1,max(dp-up,rp-lp)+1);
if (size<=min(n,m)) cout<<size*size-black<<endl;
else cout<<-1<<endl;
return 0;
}
