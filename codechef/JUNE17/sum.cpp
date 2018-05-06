#include<bits/stdc++.h>
using namespace std;
#define ll long long 
int main(){
ll t,flag;
ll qw;
ll p,q,r,x,y,z,i;
ll total,c1,c2,c3,c4,mod;
mod=1000000007;
scanf("%lld",&t);
ll result[t];
for (qw=0;qw<t;qw++){
scanf("%lld",&p);
scanf("%lld",&q);
scanf("%lld",&r);
ll A[p];
ll B[q];
ll C[r];
ll dpA[p];
ll dpC[r];
for (i=0;i<p;i++)
	scanf("%lld",&A[i]);
for (i=0;i<q;i++)
	scanf("%lld",&B[i]);
for (i=0;i<r;i++)
	scanf("%lld",&C[i]);
sort(A,A+p);
sort(B,B+q);
sort(C,C+r);
dpA[0]=A[0];
dpC[0]=C[0];
for (i=1;i<p;i++)
	dpA[i]=(dpA[i-1]%mod+A[i]%mod)%mod;
for (i=1;i<r;i++)
	dpC[i]=(dpC[i-1]%mod+C[i]%mod)%mod;
x=0;
z=0;
c1=0;
c2=0;
c3=0;
c4=0;
total=0;
flag=0;
for (i=0;i<q;i++){
	y=B[i];
	while (x<p-1){
			if (y>=A[x] && y<A[x+1]){
				break;}
			else{
				if (y<A[x]){
					flag=1;
					break;}
				if (y>=A[x+1] && y>=A[x]){
					x=x+1;
					}
				}
			}
		if (flag==1){
			flag=0;
			continue;}
		while (z<r-1){
			if (y>=C[z] && y<C[z+1]){
				break;}
			else{
				if (y<C[z]){
					flag=1;
					break;}
				if (y>=C[z+1] && y>=C[z]){
					z=z+1;}
					}
				}
		if (flag==1){
			flag=0;
			continue;}
		if (x==p-1){
			if (y>=A[x]){
				x=p-1;}
			else{
				x=p;}
		}
		if (z==r-1){
			if (y>=C[z]){
				z=r-1;}
			else{
				z=r;}
		}
		if (x!=p && z!=r){
			c1=(((z+1)*y)%mod*dpA[x])%mod;
			c2=((((x+1)*(z+1))%mod*(y*y)%mod)%mod+c1)%mod;
			c3=((((x+1)*y)%mod*dpC[z])%mod+c2)%mod;
			c4=((dpA[x]*dpC[z])%mod+c3)%mod;
			total=(total+c4)%mod;
			}
		else{
			break;}
			}
			result[qw]=total%mod;
			}
	for (i=0;i<t;i++)
		printf("%lld\n",result[i]);
	return 0;
}

