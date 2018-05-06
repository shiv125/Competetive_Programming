#include <iostream>
#include <algorithm>
#include <utility>
#include <queue>
using namespace std;
#define pi pair<int,int>
int arr[500][500];
bool stop(pi pt){
	return (pt.first == -1 and pt.second == -1);
}
int main(){
int ax[] = {1,0,-1,0,1,1,-1,-1};
int ay[] = {0,1,0,-1,1,-1,1,-1};
int t,total,n,m,max,s,x1,y1,new_x1,new_y1;
cin>>t;
int result[t];
for (int y=0;y<t;y++){
cin>>n;
cin>>m;
//int arr[n][m];
max=0;
for (int j=0;j<n;j++){
for (int k=0;k<m;k++){
cin>>s;
if (s>max)
	max=s;
arr[j][k]=s;
}
}
queue<pi> lookup;
	for(int i=0;i<n;++i)
		for(int j=0;j<m;++j)
			if(arr[i][j] == max)
				lookup.push(pi(i,j));
	lookup.push(pi(-1,-1));
	total= 0;
	while(!lookup.empty()) {
		int flag = 0,waste;
		waste=1;
		while(!stop(lookup.front())) {
			x1 = lookup.front().first;
			y1 = lookup.front().second;
			lookup.pop();	
			for(int i=0;i<8;++i){
				waste=1;
				new_x1 = x1+ax[i];
				new_y1 = y1+ay[i];
					if (new_x1<0 or new_y1<0 or new_x1==n or new_y1==m){
						waste=0;}
					else{
						if (arr[new_x1][new_y1]==max)
							waste=0;}
				if(!waste) continue;
				arr[new_x1][new_y1] = max;
				if(!flag) {total++;
				flag = 1;}
				lookup.push(pi(new_x1,new_y1));
			}
		}
		lookup.pop();
		if(!lookup.empty())
			lookup.push(pi(-1,-1));
	}

	result[y]=total;
	}
	for (int i=0;i<t;i++)
		cout<<result[i]<<endl;

	return 0;
}
