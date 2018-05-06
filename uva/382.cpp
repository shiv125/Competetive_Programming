#include <bits/stdc++.h>
 
using namespace std;
 
#define ll long long

int propdev(ll n){
int res=0;
	for (int i=2;i<(int)sqrt(n)+1;i++){
		if (n%i==0){
			if (i==n/i)
				res+=i;
			else
				res+=(i+n/i);
	}
	}
	if (n==1)
		return -1;
	res=res+1;
	if (res==n)
		return 0;
	else if (res>n)
		return 1;
	else
		return -1;

}

int main(){
ll elem;
cout<<"PERFECTION OUTPUT"<<endl;
while (true){
cin>>elem;
if (elem==0)
	break;
int t=propdev(elem);
int l=0;
ll s=elem;
while (s>0){
l+=1;
s/=10;
}
l=5-l;
for (int j=0;j<l;j++)
	cout<<' ';
cout<<elem;
if (t==0)
	cout<<"  PERFECT"<<endl;
else if (t==1)
	cout<<"  ABUNDANT"<<endl;
else
	cout<<"  DEFICIENT"<<endl;

}
cout<<"END OF OUTPUT"<<endl;
return 0;
}
