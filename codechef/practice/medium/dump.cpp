#include<bits/stdc++.h>
#define fn(i,n) for(int i=0;i<n;i++)
#define ll long long
#define wh while
#define str string
#define pb push_back
#define sc(n) scanf("%lld",&n)
using namespace std;
int main()
{
    while (true){try{
   ll n;
   sc(n);
{ll dp[1000][1000],i,j,w,l,k,sum[1000][1000];
 ll a[100005];
fn(i,n)
sc(a[i]);
fn(i,n)
{
   fn(j,n)
    {
      sum[i][j]=0;
    }
}
for(i=1;i<=n;i++)
{
    for(j=i;j<=n;j++)
    {
        if(i==0||j==0)
        sum[i][j]=0;
        else
        sum[i][j]=(sum[i][j-1]+a[j-1])%100;
    }
}
/*for(i=1;i<=n;i++)
{
    for(j=i;j<=n;j++)
    cout<<sum[i][j]<<endl;
 
}*/
fn(i,n)
dp[i][i]=0;
if(n>2)
{for(l=2;l<=n;l++)
{
    for(i=0;i<=n-l;i++)
    {
        j=l+i-1;
       
        
        dp[i][j]=1000000000;
        for(k=i;k<=j-1;k++)
        {
            dp[i][j]=min(dp[i][k]+dp[k+1][j]+sum[i+1][k+1]*sum[k+2][j+1],dp[i][j]);
    
        }
        
    
    }
}
}
else
dp[0][n-1]=a[0]*a[1];
printf("%lld\n",dp[0][n-1]);     
}
}
catch(exception const&e){
break;
}
}
	return 0;
} 
