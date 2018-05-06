#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
using namespace std;
int main(){
ll n,a,b,count,t2p;
count=0,t2p=0;
cin>>n>>a>>b;
int t[n];
f(i,n) cin>>t[i];
f(i,n){
if (t[i]==1){
	if (a>0){
		a--;}
	else{
		if (t2p>0){
			t2p--;	}
		else{
			if (b>0){
			b--;
			t2p++;}
			else{
			count++;}
			}
		}
	}
else{
if (b>0){b--;}
else{if (a>0){a--;
if (a>0){a--;}
else{
if (t2p>0){t2p--;}
else{count++;}
}}
else{if (t2p>1) {t2p-=2;} else if (t2p>0) {t2p--;count++;} else {count+=2;}}
}
}
}
cout<<count<<endl;
return 0;
}
