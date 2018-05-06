#include <iostream>
#include <algorithm>
using namespace std;
#define M_S 1000
int comp(const void* a,const void *b){
	int *A=(*(int**)a);
	int *B=(*(int**)b);
	if(A[0]!=B[0])return A[0]-B[0];
	return A[1]-B[1];
}
int **arr;
int arr2[100005];
int n,m;
int pree[110][100005];
int deg[110]={0};
int main(){
	cin>>n>>m;
	arr=new int*[n+1];
	for(int i=1;i<=n;i++){
		arr[i]=new int[2];
		cin>>arr[i][0];
		arr[i][1]=i;
		arr2[i]=arr[i][0];
	}
	qsort(arr+1,n,sizeof(int),comp);
	
	for(int i=0;i<110;i++){
		for(int e=0;e<100005;e++){
			pree[i][e]=0;
		}
	}
	for(int i=1;i<=n;i++){
		pree[(i-1)/M_S][arr[i][1]]=1;
	}
	for(int i=0;i<110;i++){
		for(int e=1;e<=n;e++){
			pree[i][e]+=pree[i][e-1];
		}
	}
	int a,b,k,tmp;
	while(m--){
		tmp=0;
		cin>>a>>b>>k;
		for(int i=0;i<110;i++){
			if(tmp+pree[i][b]-pree[i][a-1]>=k){
				for(int e=i*M_S;e<(i+1)*M_S && e<=n;e++){
					if(arr[e+1][1]>=a && arr[e+1][1]<=b){
						tmp++;
					}
					if(tmp==k){
						cout<<arr2[arr[e+1][1]]<<endl;
						break;
					}
				}
				break;
			} else {
				tmp+=pree[i][b]-pree[i][a-1];
			}
		}
	}
}
