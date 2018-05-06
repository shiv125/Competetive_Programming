#include <bits/stdc++.h> 
using namespace std;
#define f(i,n) for (int i=0;i<n;i++)
typedef signed long long int ll;
//unordered_map<ll,ll> lookup;
//string s="11111111111111111111111111111";
string s;
ll fun(ll l);
int main(){
ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	ll l;
while (true){
	string s;
	cin>>s;
	if (s=="0")
		break;
	l=s.size();
	unordered_map<ll,ll> lookup;
	//cout<<s<<l<<endl;
	cout<<fun(l)<<endl;
	}
return 0;
}
ll fun(ll l){
if (lookup.find(l)!=lookup.end()){
		return lookup[l];}
else{
	if (l>=2){
		string z;
		z+=s[l-2];
		z+=s[l-1];
		int elem=stoi(z);
		if (elem<=26){
			if (l==2){
				if (elem==10 or elem==20)
					lookup[l]=1;
				else
					lookup[l]=2;}
			else{
				if (elem==10 or elem==20){
					lookup[l]=fun(l-2);}
				else if (elem<10){
					lookup[l]=fun(l-1);}
				else{
					lookup[l]=fun(l-1)+fun(l-2);}}}
		else{	
			lookup[l]=fun(l-1);}}
	else{
		lookup[l]=1;}
	return lookup[l];
	}
}

