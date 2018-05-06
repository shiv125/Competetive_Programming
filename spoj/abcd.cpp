#include <bits/stdc++.h> 
using namespace std;
typedef long long int ll;
#include<string>
#include<string.h>
#define f(i,n) for (int i=0;i<n;i++)
ll n,n1;

char d[5]="ABCD";
int main(){
ios_base::sync_with_stdio(false);
    cin.tie(NULL);
ll ma;
cin>>n;
n1=2*n;
char s[n1+100];
cin>>s;
int res[n1];
ll count[4];
f(i,4){
count[i]=0;}
int cd=0;
f(i,n1){
if (s[i]=='A'){
	cd=0;}
else if (s[i]=='B'){
	cd=1;}
else if (s[i]=='C'){
	cd=2;}
else if (s[i]=='D'){
	cd=3;}
count[cd]+=1;}
int left,r;
ma=100000;
f(i,4){
if (d[i]!=s[0]){
if (count[i]<n){
if (ma>count[i]){
ma=count[i];
r=i;
}
break;
}}
}
res[0]=r;
left=r;
count[r]+=1;
for (int i=1;i<n1;i++){
ma=1000000;
f(j,4){
if ((d[j]!=s[i]) and (j!=left)){
	if (count[j]<n){
		if (ma>count[j]){
			ma=count[j];
			r=j;
		}
	}
}
}
count[r]+=1;
res[i]=r;
left=r;
}
int p=0;
f(i,n1){
p=res[i];
if (p==0)
cout<<'A';
else if (p==1)
cout<<'B';
else if (p==2)
cout<<'C';
else if (p==3)
cout<<'D';

}
cout<<endl;

return 0;
}
