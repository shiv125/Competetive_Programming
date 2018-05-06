#include<bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#include <unordered_map>
#include <vector>
#include<iostream>
#define fn(i,n) for(int i=0;i<n;i++)
#define wh while
#define ll long long 
#define sc(n) scanf("%lld",&n)
//typedef pair<long,long> pi;
//typedef vector<pair<long long,long long>> vp;
//typedef vector<vp> vvp;
using namespace std;
//typedef vector<int> vi;
//typedef pair<long long,long long> ii;
typedef vector<long long> vl;
typedef vector<vl> vz;
int main(){
//vector<vector<long long> > graph[100002];
//vector<vector<long long> > child[100002];
int visited[100001];
int level[100001];
int prob[100001];
ll n,u,v;
cin>>n;
for (int i=0;i<n+1;i++){
prob[i]=1;
}

//list<vector<int>> graph
vector<long long> graph[100001];
vector<long long> child[100001];
//f(i,n){
//
//}
fn(i,n-1){
cin>>u;
cin>>v;
graph[u].push_back(v);
graph[v].push_back(u);
}

queue<ll> q;
q.push(1);
ll current;
while (!q.empty()){
current=q.front();
q.pop();
if (visited[current]==0){
visited[current]=1;
fn(i,graph[current].size()){
ll v=graph[current][i];
if (visited[v]==0){
child[current].push_back(v);
q.push(v);
}}
}
}

fn(i,n+1){
visited[i]=0;
level[i]=0;
}

//queue<ll> q;
q.push(1);
while (!q.empty()){
current=q.front();
q.pop();
if (visited[current]==0){
visited[current]=1;
fn(i,graph[current].size()){
ll v=graph[current][i];
if (visited[v]==0){
if (child[current].size()>0){
prob[v]=prob[current]*child[current].size();
}
level[v]=level[current]+1;
//child[current].push_back(v)
q.push(v);
}}
}
}
float total=0.0;
if (n==1){
cout<<0.0<<endl;
}
else{
for (int i=2;i<n+1;i++){
if (graph[i].size()==1){
float t=level[i];
total+=t/prob[i];
}
}
cout<<total<<endl;
}

return 0;

}
