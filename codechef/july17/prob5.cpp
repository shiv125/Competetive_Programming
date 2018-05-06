#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
#define PB push_back
#define MP make_pair
#define f(i,n) for (int i=0;i<n;i++)
//typedef long long ll;
typedef pair<long,long> pi;
//typedef vector<pair<long long,long long>> vp;
//typedef vector<vp> vvp;
vector<pair <int,int> > graph[1000];
#define ll long long 

//vvp graph(105);
//vector<pair<ll,ll>> graph(105);
//vector<ll> graph[105];
//for(int i=0;i<105;i++){
//graph[i]=new vector<pair<ll,ll>>;
//}
long long MAX_NODES=100005;
int MAX_LOG=20;
long long P[100005][30] , parent[100005];
ll level[100005];
void preprocess(ll n){
    for(int i = 1 ; i <= n ; ++i){
        for(int j = 0 ; (1<<j) < n ; ++i){
            P[i][j] = -1; 
        }
    }

      for(int i = 1 ; i <= n ; ++i){
        P[i][0] = parent[i] ; 
    }

    for(int j = 1; (1<<j) < n ; ++j){
        for(int i = 1 ; i <= n ; ++i){
             if(P[i][j-1] != -1){
                P[i][j] = P[P[i][j-1]][j-1] ; 
            }
        }
    }
}

int LCA(int u , int v){
    if(level[u] < level[v]){
        swap(u,v) ;     
    }
    //u is the node at a greater depth/lower level
    //So we have to raise u to be at the same
    //level as v. 
    int dist = level[u] - level[v] ; 
    while(dist > 0){
        int raise_by = log2(dist);
        u = P[u][raise_by];
        dist -= (1<<raise_by) ; 
    }

    if(u == v){
        return u ; 
    }

    //Now we keep raising the two nodes by equal amount
    //Untill each node has been raised uptill its (k-1)th ancestor
    //Such that the (k)th ancestor is the lca. 
    //So to get the lca we just return the parent of (k-1)th ancestor 
    //of each node

    for(int j = MAX_LOG ; j >= 0 ; --j){
        //Checking P[u][j] != P[v][j] because if P[u][j] == P[v][j]
        //P[u][j] would be the Lth ancestor such that (L >= k) 
        //where kth ancestor is the LCA
        //But we want the (k-1)th ancestor. 
        if((P[u][j] != -1) and (P[u][j] != P[v][j])){
            u = P[u][j] ; 
            v = P[v][j] ; 
        }
    }

    return parent[u] ; //or parent[v]
}   


int main(){
int t;ll n;
cin>>t;
while (t>0){
t-=1;
cin>>n;
f(i,n+1){
graph[i].clear();
}
//ll u,v,c;
//graph.resize(n+1);
//cout<<"sdf";
f(i,n-1){
ll u,v,c;
cin>>u;
cin>>v;
cin>>c;
graph[u].push_back(make_pair(v,c));
graph[v].push_back(make_pair(u,c));
}
cout<<"abcd";
//cout<<graph[1][0].first;
unordered_map<int,int> bfs_tree;
//vector<ll> q;
cout<<"abcd";
queue<ll> q;
q.push(1);
ll v0=0;
ll current;
parent[1]=1;
bfs_tree[1]=0;
cout<<"abcd";
while (!q.empty()){
current=q.front();
q.pop();
f(i,graph[current].size()){
ll v0=graph[current][i].first;
if (bfs_tree.find(v0)!=bfs_tree.end()){
q.push(v0);
parent[v0]=current;
bfs_tree[v0]=graph[current][i].second;
}
}
}

int visited[n+1];
ll level[n+1];
f(i,n+1){
visited[i]==0;
level[i]=0;
}
q.push(1);
while (!q.empty()){
current=q.front();
q.pop();
if (visited[current]==0){
visited[current]=1;
f(i,graph[current].size()){
v0=graph[current][i].first;
level[v0]=level[current]+1;
q.push(v0);}
}
}
//preprocess(n);


 for(int i = 1 ; i <= n ; ++i){
        for(int j = 0 ; (1<<j) < n ; ++i){
            P[i][j] = -1; 
        }
    }

      for(int i = 1 ; i <= n ; ++i){
        P[i][0] = parent[i] ; 
    }

    for(int j = 1; (1<<j) < n ; ++j){
        for(int i = 1 ; i <= n ; ++i){
             if(P[i][j-1] != -1){
                P[i][j] = P[P[i][j-1]][j-1] ; 
            }
        }
    }







ll m,k,res,x,lc;
cin>>m;
f(y,m){
ll u,v,k;
cin>>u>>v>>k;
res=0;
if ((u==1) or (v==1)){
if ((u==1) and (v!=1)){
x=v;
while (x!=1){
if (bfs_tree[x]<=k){
res^=bfs_tree[x];}
x=parent[x];
}}
else if (u!=1 and v==1){
x=u;
while (x!=1){
if (bfs_tree[x]<=k){
res^=bfs_tree[x];}
x=parent[x];
}
}}
else{
lc=LCA(u,v);
x=u;
while (x!=lc){
if (bfs_tree[x]<=k){
res^=bfs_tree[x];}
x=parent[x];
}
x=v;
while (x!=lc){
if (bfs_tree[x]<=k){
res^=bfs_tree[x];}
x=parent[x];
}
}
cout<<res<<endl;
}
}





return 0;
}
