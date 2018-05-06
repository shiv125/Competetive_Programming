#include <unordered_map>
#include <vector>
#include <cstdio>
#include <algorithm>
#include<iostream>
#include <bits/stdc++.h>
#define ll long long
#define I64 ({LL a; scanf("%I64d", &a); a;})
#define rep(I, n)		for (__typeof (n) I = 0 ; I < n ; ++I)

using namespace std;

#define N 100005
//#define A 1000006
//#define BLOCK 450 // ~sqrt(N)

int a[N];
int cnt[N];
int nvc[N];
ll mcount;
//ll ans[N];
int BLOCK;
struct node {
	unsigned int L, R, i,K;
}q[N];

bool cmp(node x, node y) {
	if(x.L/BLOCK != y.L/BLOCK) {
		// different blocks, so sort by block.
		return x.L/BLOCK < y.L/BLOCK;
	}
	// same block, so sort by R value
	return x.R < y.R;
}

void add(int pos) {
	//answer+=(2*cnt[a[pos]]+1)*a[pos];
	//cnt[a[pos]]+=1;
	//above[cnt[a[pos]]]+=1;
	--nvc[cnt[a[pos]]];
	if (cnt[a[pos]]==mcount)
		mcount+=1;
	++cnt[a[pos]];
	++nvc[cnt[a[pos]]];
}

void remove(int pos) {
	//answer+=(1-2*cnt[a[pos]])*a[pos];
	//cnt[a[pos]]-=1;
	--nvc[cnt[a[pos]]];
	if (cnt[a[pos]]==mcount and nvc[cnt[a[pos]]]==0)
		mcount-=1;
	--cnt[a[pos]];
	++nvc[cnt[a[pos]]];

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int L,R;
	int n,m;
//	int a[n];
	cin>>n;
	cin>>m;
	for (int i=0;i<n+1;i++){
			cnt[i]=0;
//			above[i]=0;
		}
	//unordered_map <ll,ll> dic;
	//		int m;
	//cin>>m;
	BLOCK=(int)sqrt(n);
	ll ans[m];
	for(int i=0; i<n; i++)
		cin>>a[i];

//	for (int i=0;i<n;i++)
//		if (!dic.count(a[i]))
//			dic[a[i]]=i;
//	for (int i=0;i<n;i++)
//		a[i]=dic[a[i]];
   	for(int i=0; i<m; i++) {
		cin>>L;
		cin>>R;
		//scanf("%d%d", &q[i].L, &q[i].R);
		q[i].L=L; q[i].R=R;
		q[i].i = i;
	}

	sort(q, q + m, cmp);

	int currentL = 0, currentR = -1;
	for(int i=0; i<m; i++) {
		int L = q[i].L, R = q[i].R;
		//int K=q[i].K;
		while(currentL < L) {
			remove(currentL);
			currentL++;
		}
		while(currentL > L) {
			add(currentL-1);
			currentL--;
		}
		while(currentR < R) {
			add(++currentR);
			//currentR++;
		}
		while(currentR > R+1) {
			remove(currentR);
			currentR--;
		}
	//	if (q[i].L==q[i].R)
	//		ans[q[i].i]=1;
	//	else
			ans[q[i].i] = mcount;
	}

for (int i=0;i<m;i++){
        cout<<ans[i]<<endl;
    }
	
	return 0;
	}
