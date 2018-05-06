import java.util.*;
public class Main{
	public static void main(String[] args){
		Scanner scan=new Scanner(System.in);
		int t=scan.nextInt();
		int z,n,q,res;
		List<Integer> result=new ArrayList<>();
		for (int i=0;i<t;i++)
		{
			n=scan.nextInt();
			q=scan.nextInt();
			int []arr=new int[n];
			for (int j=0;j<n;j++){
				arr[j]=scan.nextInt();
			}
			Arrays.sort(arr);
		//	long[] dp=new long[n+1];
			//dp[n]=0;
			//dp[n-1]=arr[n-1];
			//for (int r=n-1;r>0;r--){
		//		dp[r-1]=(long)arr[r-1]+dp[r];
		//	}
			for (int j=0;j<q;j++){
				z=scan.nextInt();
				res=fun(arr,n,z);
				result.add(res);	
			
			}
		}
		int len=result.size();
	for(int i = 0 ; i < len ; i++){
		System.out.println(result.get(i));
	}
	}
	public static int binarysearch(int[] arr, int target)
	{
	int val,low,high,mid;
	low=0;
	high=arr.length-1;
	while (low<=high){
	mid=(low+high)/2;
	val=arr[mid];
	if (target<=arr[low]){
		return low;}
	if (target>arr[high]){
		return -1;}

	if (target==val){
		return mid;}
	else if (target>val){
		low=mid+1;}
	else{
		if (mid-1>=low && target>arr[mid-1]){
			return mid;}
		else{
			high=mid-1;}
		}
	}
	return 0;
	}
public static int zfun(int i,int index,int ki,long[] dp){
	return (index-i)*ki-(int)(dp[i]-dp[index]);}

public static int fun(int[] arr,int n,int ki){
int i=binarysearch(arr,ki);
int temp=0;
int count;
if (i==-1){
count=0;
i=n;
}
else{
count=n-i;
}
while (i>0)
{
temp=temp+ki-arr[i-1];
if (i-1<temp){
	break;}
else{
	count=count+1;
}
i=i=1;
}
return count;
//temp=search(i/2,i-1,i,dp,ki);
//if (temp==-1){
//	return count;}
//return count+i-temp;
}
public static int search(int low,int high,int index,long[] dp,int ki){
int mid,zmid,h;
while (true){
	mid=(low+high)/2;
	if (low>=zfun(low,index,ki,dp)){
		return low;
		}
	h=zfun(high,index,ki,dp);
	if (high<h){
		return -1;}
	zmid=zfun(mid,index,ki,dp);

	if (mid==zmid){
		return mid;}
	else if (mid<zmid){
			low=mid+1;
			}
	else{
		if (mid-1<zfun(mid-1,index,ki,dp)){
			return mid;}
		else{
			high=mid-1;
		}
	}
}
}
}
