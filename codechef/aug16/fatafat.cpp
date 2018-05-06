#include<bits/stdc++.h>
#include<unordered_map>
#include<iostream>
#include<cstdio>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#define fn(i,n) for(int i=0;i<n;i++)
#define wh while
#define ll long long
#define sc(n) scanf("%lld",&n)
#define ma 1000002
using namespace std;
ll t,n;
ll arr[ma];
ll ans,k;
ll visited[ma];
int main(){
ios_base::sync_with_stdio(false);
cin.tie(NULL);
cin>>t;
while (t>0){
	t-=1;
	ll j;
	cin>>n;
	for (int i=0;i<n;i++)
		cin>>arr[i];
	int count=0;
	for (int i=0;i<n;i++)
		visited[i]=0;
	ans=0;
	for (int i=0;i<n;i++){
		if (visited[i]==0){
			count+=1;
			visited[i]=count;
			j=(i+arr[i]+1)%n;
			while (visited[j]==0){
				visited[j]=count;
				j=(j+arr[j]+1)%n;}
			if (visited[j]==count){
				ans+=1;
				k=(j+arr[j]+1)%n;
				while (k!=j){
					ans+=1;
					k=(k+arr[k]+1)%n;}
					}
		}}
	cout<<ans<<endl;}
	return 0;
	}


