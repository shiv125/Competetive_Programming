#include<bits/stdc++.h>
#define fn(i,n) for(int i=0;i<n;i++)
#define wh while
#define ll long long
#define sc(n) scanf("%lld",&n)
#define mx 12500
using namespace std;
int main(){
	ll t;
	cin>>t;
	while (t--){
		ll N,K,count2,total;
		sc(N);sc(K);
		bool lookup[K+1];
		fn(i,K+1){
		lookup[i]=false;
		}
		ll all_list[N][K+1];
		fn(i,N){
			sc(all_list[i][0]);
			fn(j,all_list[i][0]){
				sc(all_list[i][j+1]);
			}
		}	
	total=0;
	fn(i,N){
		ll count1=0;
		fn (m,all_list[i][0]){
			lookup[all_list[i][m+1]]=true;
		}
count1=all_list[i][0];
ll count2=0;
for (int j=i+1;j<N;j++){
count2=0;
if (count1+all_list[j][0]>=K){
	fn(m,all_list[j][0]){
	  if (lookup[all_list[j][m+1]]==false)
			count2=count2+1;
	}
	if (count1+count2==K)
		total+=1;
}
}
fn(m,all_list[i][0])
	lookup[all_list[i][m+1]]=false;
}
cout<<total<<endl;
}
return 0;
}
