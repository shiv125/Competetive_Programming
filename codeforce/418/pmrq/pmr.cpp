#include<bits/stdc++.h>
#include <unordered_map>
#include <vector>
#include<iostream>
#define fn(i,n) for(int i=0;i<n;i++)
#define wh while
#define ll long long
#define sc(n) scanf("%lld",&n)
#define MAP 78498
#define MAX 1000002
using namespace std;
static ll prime[MAX+1];
static ll all_primes[MAP];
static ll primes[MAX];
static ll lookup[MAP];
int main(){
	//typedef pair<long, long> pll;
	ll elem,curr,count,total,t;
	//ll primes[MAX];
 	for (ll i=0;i<MAP;i++)
		lookup[i]=0;
	for (ll i=0;i<MAX;i++){
	primes[i]=i;
	}
	for (ll j=4;j<MAX;j+=2){
	primes[j]=2;
	}
	ll i=3;ll j;
	while (i*i<MAX){
	if (primes[i]==i){
		j=i*i;
		while (j<MAX){
			if (primes[j]==j){
				primes[j]=i;}
			j=j+i;
		}
		}
		i+=1;			
	}
	//long prime[100000];
	
	for (ll j=0;j<MAX+1;j++){
	prime[j]=1;
	}
	//cout<<prime[1]<<endl;
	ll r=0;
	ll p=2;	
	while (p*p<=MAX){	
		if (prime[p]==1){
			for (ll i=p*2;i<MAX+1;i+=p){
				prime[i]=0;}}
		p+=1;
		}
	for (ll j=2;j<MAX;j++){
		if (prime[j]==1){
			all_primes[r]=j;
			r+=1;
	}
	}
	unordered_map <ll,ll> dic;
	for (ll i=0;i<MAP;i++){
	//dic.put(all_primes[i],i);
	dic[all_primes[i]]=i;
	//cout<<all_primes[i]<<endl;
	//cout<<dic[all_primes[i]]<<endl;
	}
 sc(t);
 while (t--){
ll n,m;
	sc(n);
	ll arr[n];
	for (ll i=0;i<n;i++){
	sc(arr[i]);
	}

//vector<pair<ll, ll>> lookup[n];
//ll lookup[n][2];
 
//ll bucket=n/Size;
for (ll i=0;i<n;i++){
elem=arr[i];
curr=primes[elem];
count=1;
while (elem>1)
{
elem=elem/primes[elem];
if (curr==primes[elem]){
count+=1;
continue;
}
lookup[dic[curr]]+=count;
curr=primes[elem];
count=1;
}
}
total=1;
for (ll i=0;i<MAP;i++){
	total*=(lookup[i]+1);
	lookup[i]=0;}
cout<<total<<endl;

}
return 0;
}

