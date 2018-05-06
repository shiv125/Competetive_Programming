#include <bits/stdc++.h> 
using namespace std;
typedef long long int ll;

ll power(ll a,ll b,ll mod){
	ll x=1;
	ll y=a;
	while (b>0){
		if (b%2==1){
			x=x*y;
			if (x>mod)
				x%=mod;
		}
		y=y*y;
		if (y>mod)
			y%=mod;
		b/=2;	
	}
	return x;
}
ll modinverse(ll i, ll mod){
return power(i,mod-2,mod)%mod;
}
int main(){
ios_base::sync_with_stdio(false);
    cin.tie(NULL);
ll t,n,p,res;
cin>>t;
while (t>0){
t-=1;
cin>>n;
cin>>p;
res=p-1;
if (n>=p){
	cout<<0<<endl;}
else{
	for (int j=n+1;j<p;j++){
		//cout<<modinverse(j,p)<<endl;
		//res+=p;
		res*=(modinverse(j,p));
		res%=p;
		}
	cout<<res<<endl;}
}
return 0;}
