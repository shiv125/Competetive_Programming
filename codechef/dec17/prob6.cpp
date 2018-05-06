#include<bits/stdc++.h>
#define ll long long

using namespace std;
int main(){
ll t,X,Y,Z,A,B,C,total,p,q,temp,temp2,curr,a,mi,res,t1,t2,t3,pp;
cin>>t;
pp=100000000;
while (t>0){
cin>>X>>Y>>Z>>A>>B>>C;
t-=1;
ll arr[3];
arr[0]=X;
arr[1]=Y;
arr[2]=Z;
sort(arr,arr+3);
ll fina[10];

for (int i=0;i<10;i++)
fina[i]=pp;

curr=arr[0]+arr[1]+arr[2];
fina[0]=A*curr;
temp=curr;
if (temp%2==0){
	if (temp/2>arr[2])
		fina[1]=(temp/2)*B;
}
if ((X==Y) && (Y==Z))
	fina[2]=C*X;
ll let;
let=arr[0]+arr[1];
let=min(let,arr[2]);
total=0;
total+=let*B;
total+=(curr-2*let)*A;
fina[3]=total;
total=arr[0]*C;
total+=(curr-3*arr[0])*A;
fina[4]=total;
total=C;
temp2=arr[0]+arr[1]-2;
temp2=min(temp2,arr[2]-1);
total=total+temp2*B;
total+=(curr-3-2*temp2)*A;
fina[5]=total;
total=C;
temp2=curr-3;
temp=arr[2]-1;
if (temp2%2==0){
	if (temp2/2>temp){
		total+=(temp2/2)*B;
		fina[6]=total;}
		}
total=0;
temp2=arr[2]-arr[1];
total+=(arr[0]-temp2)*C;
if (arr[0]-temp2>=0)
	fina[7]=total+(temp2+arr[2]-arr[0])*B;

total=A;
temp=curr-1;
temp2=arr[2]-1;
if (temp%2==0){
	if (temp/2>arr[2]-1)
		fina[8]=total+(temp/2)*B;
}

a=fina[0];
for (int i=1;i<10;i++){
	//cout<<fina[i-1]<<endl;
	if (fina[i]<a)
		a=fina[i];
}

mi=arr[0];
if (mi%2==0){
total=min(3*A*mi,(3*B*mi)/2);
total=min(C*mi,total);
p=arr[1]-mi;
q=arr[2]-mi;

temp2=min(A*(p+q),B*min(p,q)+A*(max(p,q)-min(p,q)));
total=total+temp2;
res= min(total,a);

}
else{
mi=mi-1;
total=min(3*A*mi,(3*B*mi)/2);
total=min(C*mi,total);
ll p1,q1,p2,q2,p3,q3;
p1=arr[1]-mi;
q1=arr[2]-mi-1;
ll t1,t2,t3;
t1=0;t2=0;t3=0;
t1=min(A*(p1+q1),B*min(p1,q1)+A*(max(p1,q1)-min(p1,q1)))+B;
p2=arr[1]-mi-1;
q2=arr[2]-mi-1;
t2=min(A*(p2+q2),B*min(p2,q2)+A*(max(p2,q2)-min(p2,q2)))+C;
p3=arr[1]-mi;
q3=arr[2]-mi;
t3=min(A*(p3+q3),B*min(p3,q3)+A*(max(p3,q3)-min(p3,q3)))+A;
t3=min(t3,t2);
total=total+min(t1,t3);

res= min(total,a);

}
cout<<res<<endl;

}
return 0;
}
