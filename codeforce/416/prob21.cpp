#include <algorithm>
#include <iostream>
#include <cstring>
#include <cassert>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>
#include <stack>
#include <cmath>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <typeinfo>
#define For(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define FOR(i,a) For(i,1,a)
#define Ford(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define Rep(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
#define REP(i,a) Rep(i,0,a)
#define type(x) __typeof(x.begin())
#define foreach(it,x) for(__typeof(x.begin()) it = x.begin() ; it!=x.end() ; it++ )

#define compress(x) {sort(all(x));(x).resize(unique(all(x))-(x).begin());}
#define fill(x,y) memset(x,y,sizeof x)
#define all(x) x.begin(),x.end()
#define two(x) (1LL<<(x))
#define fi first
#define se second
#define gcd __gcd
#define pb push_back
#define mp make_pair

#ifdef KAZAR
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
    #define dbg(x) cerr<<#x<<":"<<(x)<<endl
    #define dg(x) cerr<<#x<<":"<<(x)<<' '
#else
    #define eprintf(...) 0
    #define dbg(x) 0
    #define dg(x) 0
#endif

using namespace std;

typedef long long Lint;
typedef long double ld;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int inf = 1e9+5143;
const Lint Linf = 1e18+5413;
const double eps = 1e-10;
const double pi = acos(-1);

template<class T> inline void umax(T &a,T b){if(a<b) a = b ; }
template<class T> inline void umin(T &a,T b){if(a>b) a = b ; }
template<class T> inline T abs(T a){return a>0 ? a : -a;}
template<class T> inline T lcm(T a,T b){
	return a/gcd(a,b)*b;
}

inline int read(){
    int res = 0LL ;int neg ;
    while(1){
        char ch = gtechar();
        if(ch>='0' && ch<='9' || ch=='-'){
            if(ch=='-') neg = -1;
            else neg = 1 , res = ch-'0';
            break;
        }
    }
    while(1){
        char ch = gtechar();
        if(ch>='0' && ch<='9') res*=10,res+=ch-'0';
        else break;
    }
    return res*neg;
}

const int N = 171717;

int kd[20][N] , a[N] , pos[N] , Real[N];
int are,op;
void init(int d,int b,int e){
    if(b == e){
        kd[d][b] = pos[b];
        return;
    }
    int m = (b + e) >> 1;
    init(d + 1,b,m);
    init(d + 1,m+1,e);
    int i = b , j = m + 1;
    int ptr = 0;
    while(i <= m && j <= e){
        if(kd[d + 1][i] < kd[d + 1][j]){
            kd[d][b + (ptr++)] = kd[d + 1][i++];
        }else{
            kd[d][b + (ptr++)] = kd[d + 1][j++];
        }
    }
    while(i <= m) kd[d][b + (ptr++)] = kd[d + 1][i++];
    while(j <= e) kd[d][b + (ptr++)] = kd[d + 1][j++];
}

inline int find(int d,int b,int e,int x1,int x2){
    return upper_bound(kd[d] + b,kd[d] + e + 1,x2) - lower_bound(kd[d] + b,kd[d] + e + 1,x1);
}

int gte(int n,int x1,int x2,int k){
    int d = 0 , b = 1 , e = n;
    while(b != e){
        int ll = find(d + 1,b,(b+e)/2,x1,x2);
        int m = (b + e) >> 1;
        if(ll >= k){
            e = m;
        }else{
            b = m + 1;
            k -= ll;
        }
        ++d;
    }
    return b;
}

int main(){

#ifdef KAZAR
	freopen("f.i","r",stdin);
	freopen("f.cik","w",stdout);
	freopen("error","w",stderr);
#endif

    int n = read();
    int m = read();

    vi valles;

    FOR(i,n){
        a[i] = read();
        valles.pb(a[i]);
    }

    sort(all(valles));

    FOR(i,n){
        int old = a[i];
        a[i] = lower_bound(all(valles),a[i]) - valles.begin() + 1;
        pos[a[i]] = i;
        Real[a[i]] = old;
    }

    init(0,1,n);
	int ze;
    while(m--){
        int from = read(), to = read(), k = read();
		if (k>to){
			printf("%s\n","Yes");}
		else if (k<from){
			printf("%s\n","Yes");
		}
		else{
        //assert(to - from + 1 >= k);
		are=k-from+1;
        op=Real[gte(n,from,to,are)];
	//std::cout<<"a is of type: "<<typeid(a[1]).name()<<std::endl; // Output 'a is of type int'
    //std::cout<<"b is of type: "<<typeid(op).name()<<std::endl; // Output 'b is of type someClass
		if (op-a[k]==0){
			printf("%s\n","Yes");
			}
		else{
			printf("%s\n","No");
		}
		
		}
		}

    return 0;
}
