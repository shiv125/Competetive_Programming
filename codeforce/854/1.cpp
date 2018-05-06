#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
using namespace std;
int main(){
int n;
cin>>n;
if (n%2==0){if ((n/2)%2){cout<<n/2-2<<" "<<n/2+2<<endl;} else{cout<<n/2-1<<" "<<n/2+1<<endl;}}
else{cout<<n/2<<" "<<n/2+1<<endl;}
return 0;
}
