#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
using namespace std;
int main(){
ll n,k;cin>>n>>k;
if (k==0 or k==n){
cout<<0<<" "<<0<<endl;}
else{
if (n/3>=k) cout<<1<<" "<<2*k<<endl;
else cout<<1<<" "<<n-k<<endl;}
return 0;
}
