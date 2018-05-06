#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#define rf freopen("in.in", "r", stdin)
#define wf freopen("out.out", "w", stdout)
#define rep(i, s, n) for(int i=int(s); i<=int(n); ++i)
using namespace std;
const int mx=1e5+10,mod=1e9+7;
int n,t;
//int arr[mx];
//int product[mx];

int main(){
ios::sync_with_stdio(0);
//scanf("%d",&t);
cin>>t;
while (t--){
	//scanf("%d",&n);
	cin>>n;
	n+=1;
	int arr[n+1];
	int product[n+1];
	for (int i=1;i<n+1;++i)
		//scanf("%d",&arr[i]);
		cin>>arr[i];
	int pow2=1;
	for (int i=n;i>0;--i){
		product[i]=(1ll*arr[i]*pow2)%mod;
		if (i<n)
			product[i]=(product[i+1]+product[i])%mod;
		pow2=(pow2*2)%mod;
	}
	pow2=1;
	int total=0;
	for (int i=1;i<n;++i){
		int elem=(1ll*arr[i]*pow2)%mod;
		total=(total+(1ll*product[i+1]*elem)%mod)%mod;
		if (i>=2)
			pow2=(2*pow2)%mod;
	}
	cout<<(2*total)%mod<<'\n';
}
return 0;
}

