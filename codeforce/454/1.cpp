#include<bits/stdc++.h>
#define ll long long
#define f(i,n)  for (int i=0;i<n;i++)
using namespace std;
int hurray[150005];
int main(){
ll n,m,temp,ind;
cin>>n>>m;
if (n==1 and m==1) cout<<"YES"<<endl<<1<<endl;
else if (n<3 and m<3){cout<<"NO"<<endl;}
else if (m==1 and n<5){cout<<"NO"<<endl;}
else if (m==3 and n==2){cout<<"NO"<<endl;}
else if (m==2 and n==3){cout<<"NO"<<endl;}
else if (m<5 and n==1){cout<<"NO"<<endl;}
else if (m==1 or n==1){
int flag=0;
if (m<n){temp=n;n=m;m=temp;flag=1;}
temp=100000;
hurray[temp]=1;hurray[temp+1]=3;hurray[temp+2]=5;hurray[temp+3]=2;
hurray[temp+4]=4;
temp+=5;
int l=6;
m=m-5;
ll c=6;
for (int y=m/2+1;y>0;y--){
hurray[temp]=l;
l++;
hurray[temp-c]=l;
c+=2;
temp++;l++;
}
c-=2;
if (m%2) {hurray[temp]=l;}
if (flag){
if (m%2==0){
for(int j=temp-c;j<temp-1;j++)
	cout<<hurray[j]<<endl;
}
else{
for(int j=temp-c;j<temp;j++)
	cout<<hurray[j]<<endl;

}

}
else{
if (m%2==0){
for(int j=temp-c;j<temp-1;j++)
	cout<<hurray[j]<<" ";cout<<endl;
}
else{
for(int j=temp-c;j<temp;j++)
	cout<<hurray[j]<<" ";
cout<<endl;}
}
}

else{
ll store[n][m];
ll ind2;
temp=2;
store[0][0]=n*m;
for (int i=1;i<m;i++){ind=i;
for (int j=0;j<n;j++){store[j][ind]=temp;temp++;ind--; if (ind<0) break;}
}
for (int i=1;i<n-1;i++){
ind=i;
ind2=m-1;
for (int j=ind;j<n;j++){
store[j][ind2]=temp;
temp++;
ind2--;
if (ind2<0) break;
}
}
store[n-1][m-1]=1;


cout<<"YES"<<endl;
f(i,n){f(j,m) cout<<store[i][j]<<" "; cout<<endl;}
}
return 0;
}
