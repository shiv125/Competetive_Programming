#include<bits/stdc++.h>
#define ll long long 
using namespace std;
ll helper(ll n,ll mod){
	ll res=1;
	ll ori=n;
	ll a=0;
	while (n)
	{
		a*=10;
		a+=n%10;
		res*=10;
		n/=10;
		res%=mod;
		a%=mod;
	}
	return ori*res+a;
}
int main(){
ll k,p,tot;
tot=0;
cin>>k>>p;
for (int m=1;m<k+1;m++){
tot=(tot+helper(m))%p;
}
cout<<tot<<endl;
return 0;
}
