#include <bits/stdc++.h> 
using namespace std;
#define f(i,n) for (int i=0;i<n;i++)
typedef long long int ll;
int main(){
ios_base::sync_with_stdio(false);
    cin.tie(NULL);
ll n,k,total;
total=0;
cin>>n;cin>>k;
ll arr[n];
unordered_map<ll,int> count;
f(i,n){
cin>>arr[i];
count[arr[i]]=1;
}
sort(arr,arr+n);
f(i,n){
if (count.find(arr[i]+k)!=count.end())
	total+=1;
}
cout<<total<<endl;
return 0;
	}
