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
ll arr[ma];
int main(){
ios_base::sync_with_stdio(false);
    cin.tie(NULL);
int t,flag;
ll n,temp;
cin>>t;

while (t>0){
t-=1;
flag=0;
cin>>n;

//unordered_map <ll,ll> lookup;
for (int i=0;i<n;i++){
cin>>arr[i];
//lookup[arr[i]]=i;
}
for (int i=1;i<n;i++){
	if (arr[i]<arr[i-1]){
		temp=arr[i];
		arr[i]=arr[i-1];
		arr[i-1]=temp;
	}
}
//sort(arr,arr+n);
for (int i=1;i<n;i++){
	if (arr[i]<arr[i-1]){
		flag=1;
		break;
	}
}
if (flag)
	cout<<"NO"<<endl;
else
	cout<<"YES"<<endl;
	

}
return 0;
}
