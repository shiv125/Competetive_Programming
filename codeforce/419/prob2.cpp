#include <queue>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <bitset>
#include <cstdlib>
#include <list>
#include <stack>
#include <deque>
#include <cmath>
#include <string>
#include <string.h>
#include <iomanip>
using namespace std;
#define rep(i,n) for(int i = 0;  i < n ; ++i)
#define REP(i,a,b) for(int i = a ; i <= b ; ++i)
#define s(n) scanf("%d",&n)
#define rev(i,n) for(int i = n ; i >= 0 ; --i)
#define REV(i,a,b) for(int i = a ; i >= b ; --i)
#define miN(a,b) (((a)<(b))?(a):(b))
#define sc(n) scanf("%c",&n)
#define scan(n) scanf("%lld",&n)
#define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define INF 1000000000 
#define pp pair<int,int> 
#define pb(a) push_back(a)
#define ll long long 
struct SegTree{
	long long sum ; 
	long long update ;  
};
 
 
static SegTree tree[8*100000] = {0} ; 
 
 
void build_tree(int node , int a , int b )
{
	tree[node].update = 0 ; 
	tree[node].sum = 0 ; 
	if(a == b)
	{
		tree[node].sum = 0 ; 
		return ;  
	}
	build_tree(2*node , a , (a+b)/2) ;
	build_tree(2*node + 1 , (a+b)/2 + 1 , b) ;
 
}
 
void update(int node , int a , int b , int i , int j , long long v)
{
	if(tree[node].update)
	{
		tree[node].sum += tree[node].update*(b - a + 1) ; 
		if(a != b)
		{
			tree[2*node].update += tree[node].update ;
			tree[2*node + 1].update += tree[node].update ; 
		}
		tree[node].update = 0 ; 
	}
	if(i > b || j < a)
	{
		return ; 
	}
 
	if(a >= i && b <= j)
	{
		tree[node].sum += v*(b - a + 1) ;
		if(a != b)
		{
			tree[2*node].update += v ;
			tree[2*node + 1].update += v ; 
		}
		return ; 
	}
	update(2*node , a , (a+b)/2 , i , j , v) ;
	update(2*node + 1 , (a+b)/2 + 1 , b , i , j , v) ;
	tree[node].sum = min(tree[2*node].sum ,tree[2*node + 1].sum) ; 
 
}
 
long long query(int node ,int a , int b , int i , int j)
{
	if(tree[node].update)
	{
		tree[node].sum += tree[node].update*(b - a + 1) ; 
		if(a != b)
		{
			tree[2*node].update += tree[node].update ;
			tree[2*node + 1].update += tree[node].update ; 
		}
		tree[node].update = 0 ; 
	}
	if(i > b || j < a)
	{
		return 0; 
	}
	if(a >= i && b <= j)
	{
		return tree[node].sum ; 
	}
 
	return (query(2*node , a , (a+b)/2 , i , j) + query(2*node + 1 , (a+b)/2 + 1 , b , i , j)) ;
}
 
static ll arr[200001]; 
int main() 
{
	//freopen("input.txt","r",stdin) ;
	int N , type,  Q;
	long long v , ans; 
	//ll arr[200001];
	N=200001;
	ll n,k,q,r,l,res,x,y;
	int tc ;
	scan(n);scan(k);scan(q); 
	//while(tc--)
	//{
	//	s(N) ;
		build_tree(1,1,N) ;
	//	s(Q) ;
		while(n--)
		{
		//	s(type) ;
		//	s(x) ;
		//	s(y) ;
		//	if(type == 1)
		//	{
		//		ans = query(1,1,N,x,y) ; 
		//		printf("%lld\n",ans) ; 
		//	}
		//	else
		//	{
			//	scanf("%lld",&v) ;
				scan(x);scan(y);
				update(1,1,N,x,y,1) ; 
		//	}
		}
		for (int i=1;i<200001;i++)
			arr[i]=query(1,1,200001,i,i);
		for (int i=1;i<200001;i++)
			if (arr[i]>=k)
				arr[i]=1;
			else
				arr[i]=0;
		for (int i=1;i<200001;i++)
			arr[i]+=arr[i-1];

		while (q--){
			scan(l);scan(r);
			res=arr[r]-arr[l-1];
			cout<<res<<endl;
		}
	
	
	//}
	return 0 ;
}
