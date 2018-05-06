#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
#define PI acos(-1)
#define sqr(x) ((x) * (x))
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ALL(c) (c).begin(), (c).end()
#define SIZE(c) (int)(c).size()
#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)
#define REPD(i, a, b) for (int i = int(a); i >= int(b); i--)
typedef unsigned long long ull;
typedef long long ll;
typedef pair<int,int> ii;
typedef pair<double,double> dd;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef map<int,int> mii;
typedef set<int> si;
const int MAXN=100000;
int V[MAXN+1]={0}, E[2*MAXN]={0}, L[2*MAXN]={0}, H[MAXN+1]={0}, P[MAXN+1]={-1}, K=0;

ll N,LCA;
bool disc[MAXN+1]={false};
vvi g;
class SparseTable {
private: 
	int **M, N, LOGN, *A;
public:
	SparseTable(int N_, int A_[]) {
		N = N_, A = A_, LOGN = ceil(log2(N));
		M = new int*[N];
		REP(i, 0, N-1) {
			M[i] = new int[LOGN];
			memset(M[i], 0, LOGN * sizeof(int));
		}
		REP(i, 0, N-1) { M[i][0] = i; }
		for (int j = 1; 1 << j <= N; j++) {
		    for (int i = 0; i + (1 << j) - 1 < N; i++) {
		        if (A[M[i][j - 1]] < A[M[i + (1 << (j - 1))][j - 1]]) {
		            M[i][j] = M[i][j - 1];
		        } else {
		            M[i][j] = M[i + (1 << (j - 1))][j - 1];
		        }
		    }
		}
	}
    int query(int i, int j) { 
        int k = log2(j - i + 1);
        if(A[ M[i][k] ] <= A[ M[j - (1<<k) + 1][k] ]) { return M[i][k]; }
        else { return M[j - (1<<k) + 1][k]; }
    }
};
void dfs(int v, int d, int &k) {
    H[v] = k;
    E[k] = v;
    L[k++] = d;
    disc[v]=true;
    REP(i, 0, SIZE(g[v])-1) {
    	int u = g[v][i];
        if (!disc[u]) {
            P[u] = v;
            dfs(u, d+1, k);
            E[k] = v;
            L[k++] = d;
        }
    }
}
void init_search() { REP(i, 0, MAXN) { disc[i]=false; } }
#define PROD //clocking off
int main() {
#ifndef PROD
//clock_t stop_s,start_s;
#endif
    //init tree
	int t;
	ll m;
	cin>>t;
	while (t>0){
	t-=1;
	ll x,y;
    cin >> N;
    g.resize(N+1);
    REP(i, 1, N-1) {
        cin >> x >> y;
        g[x].PB(y);
        g[y].PB(x);
    }
    dfs(1, 0, K); //tree is rooted at 1
    SparseTable ST(2*N, L);
	cin>>m;
	for (ll er=0;er<m;er++){
    ll a, b;
    cin >> a >> b; //for example ..
    //get LCA of a,b
    LCA = E[ST.query(min(H[a], H[b]), max(H[a], H[b]) + 1)];
	cout<<LCA<<endl;
	
	}
	
	}
#ifndef PROD
//stop_s=clock();
//cout << "time: " << (stop_s-start_s)/double(CLOCKS_PER_SEC)*1000 << endl;
#endif
	return 0;
}
