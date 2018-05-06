#include<bits/stdc++.h>
#include <unordered_map>
#include <vector>
#include<iostream>
#define fn(i,n) for(int i=0;i<n;i++)
#define wh while
#define ll long long
#define sc(n) scanf("%lld",&n)
#define mx 12500
#define MAP 78498
#define MAX 1000002
using namespace std;
ll binarysearch(ll arr[], ll low, ll high, ll x);
ll binarysearchfloor(ll arr[], ll low, ll high, ll x);


/**

       if (low > high)
        return -1;
 
     if (x >= arr[high])
        return high;
 
       ll mid = (low+high)/2;
 
   
    if (arr[mid] == x)
        return mid;
 
   
    if (mid > 0 and arr[mid-1] <= x and x < arr[mid])
        return mid-1;
 
    if (x < arr[mid])
        return binarysearchfloor(arr, low, mid-1, x);
 	if (x>arr[mid])
   		return binarysearchfloor(arr, mid+1, high, x);
**/

static ll prime[MAX+1];
static ll all_primes[MAP];
static ll primes[MAX];
int main(){
	//typedef pair<long, long> pll;
	ll elem,curr,count,L,R,X,Y,fi,si,ans,l_b,r_b,R1,L2;
	//ll primes[MAX];

	fn(i,MAX){
	primes[i]=i;
	}
	for (int j=4;j<MAX;j+=2){
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
	
	for (int j=0;j<MAX+1;j++){
	prime[j]=1;
	}
	//cout<<prime[1]<<endl;
	int r=0;
	ll p=2;	
	while (p*p<=MAX){	
		if (prime[p]==1){
			for (int i=p*2;i<MAX+1;i+=p){
				prime[i]=0;}}
		p+=1;
		}
	for (int j=2;j<MAX;j++){
		if (prime[j]==1){
			all_primes[r]=j;
			r+=1;
	}
	}
	
	
	unordered_map <int,int> dic;
	fn(i,MAP){
	//dic.put(all_primes[i],i);
	dic[all_primes[i]]=i;
	}

ll n,m;
	sc(n);
	ll arr[n];
	fn(i,n){
	sc(arr[i]);
	}
	sc(m);
	ll Size;
	ll dp[MAP][Size];
ll result[m];
if (n>=20000 and n<=100000){
	Size=n/170;}
else if (n<10000 and n>=2000){
	Size=n/120;}
else{
	Size=n/50;}
if (Size==0){
	Size=1;}
vector<pair<long, long>> lookup[n];
//ll lookup[n][2];

ll bucket=n/Size;
fn(i,n){
elem=arr[i];
curr=primes[elem];
count=1;
pair<long,long> pair1;
while (elem>1)
{
elem=elem/primes[elem];
if (curr==primes[elem]){
count+=1;
continue;
}
dp[dic[curr]][i/bucket]+=count;
pair1.first=curr;pair1.second=count;
lookup[i].push_back(pair1);
curr=primes[elem];
count=1;
}
}
fn(i,MAP){
for (int j=1;j<Size;j++){
	dp[i][j]+=dp[i][j-1];}}
fn(i,Size){
for (int j=1;j<MAP;j++){
	dp[j][i]+=dp[j-1][i];}}
ll len;
fn(i,m){
sc(L);sc(R);sc(X);sc(Y);
fi=binarysearch(all_primes,0,MAP-1,X);
si=binarysearchfloor(all_primes,0,MAP-1,Y);
ans=0;
if (fi!=-1){
l_b=(L-1)/bucket;
		r_b=(R-1)/bucket;
		if (r_b-l_b<=1){
			for (int j=L-1;j<R;j++){
				len=lookup[j].size();
				fn(it,len){
					if (lookup[j][it].first>=X and lookup[j][it].first<=Y){
						ans+=lookup[j][it].second;}
					if (lookup[j][it].first>Y){
						break;}
						}
						}
				}
				
		else{
			if (fi!=0)
				ans+=dp[si][r_b-1]-dp[si][l_b]-(dp[fi][r_b-1]-dp[fi][l_b]);
			else
				ans+=dp[si][r_b-1]-dp[si][l_b];
			R1=(l_b+1)*bucket;
			for (int j=L-1;j<R1;j++){
				len=lookup[j].size();
				fn(it,len){
					if (lookup[j][it].first>=X and lookup[j][it].first<=Y)
						ans+=lookup[j][it].second;
					if (lookup[j][it].first>Y)
						break;
						}
						}
			L2=(r_b)*bucket;
				for (int j=L2;j<R;j++){
				len=lookup[j].size();
				fn(it,len){
					if (lookup[j][it].first>=X and lookup[j][it].first<=Y)
						ans+=lookup[j][it].second;
					if (lookup[j][it].first>Y)
						break;
						}
						}
			}
			}
	result[i]=ans;
	}
	fn(i,m){
		printf("%lld\n",result[i]);
	}
	
	return 0;
	}

ll binarysearch(ll arr[], ll low, ll high, ll x)
{ 
ll mid;
while (low<=high){
if (x<=arr[low])
	return low;
if (x>arr[high]){
return -1;}
mid=(low+high)/2;
if (arr[mid]<x){
if (mid+1<=high and x<=arr[mid+1])
	return mid+1;
else
	low=mid+1;
}
else{
if (mid-1>=low and x>arr[mid-1])
	return mid;
else
	high=mid-1;
}
}

return -1;
 }

ll binarysearchfloor(ll arr[], ll low, ll high, ll x)
{
ll mid;
while (low<=high){
if (low>high)
	return -1;
if (x>=arr[high])
	return high;
mid=(low+high)/2;
if (arr[mid]==x)
	return mid;
if (mid>0 and arr[mid-1]<=x and x<arr[mid]){
	return mid-1;
}
if (x<arr[mid])
	high=mid-1;
if (x>arr[mid])
	low=mid+1;

}
return -1;
}
