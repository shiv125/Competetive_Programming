/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner scan=new Scanner(System.in);
		int t=scan.nextInt();
		int z,n,q,res;
		List<Integer> result=new ArrayList<>();
		for (int i=0;i<t;i++)
		{
		    if (scan.hasNext()){
			    n=scan.nextInt();
		    }
			if (scan.hasNext()){
			    q=scan.nextInt();
			}
			int []arr=new int[n];
			for (int j=0;j<n;j++){
			    if (scan.hasNext()){
				    arr[j]=scan.nextInt();
			}
			    
			}
			Arrays.sort(arr);
			int[] dp=new int[n+1];
			dp[n]=0;
			dp[n-1]=arr[n-1];
			for (int r=n-1;r>0;r--){
				dp[r-1]=arr[r-1]+dp[r];
			}
			for (int j=0;j<q;j++){
			    if (scan.hasNext())
				    z=scan.nextInt();
				res=fun(arr,n,z,dp);
				result.add(res);	
			
			}
		}
		int len=result.size();
	for(int y = 0 ; y < len ; y++){
		System.out.println(result.get(y));
	}
	}
	public static int binarysearch(int[] arr, int low, int high, int x)
	{
		int mid=0;
	if (x<=arr[low]){
		return low;
		}
	if (x>arr[high]){
		return -1;}
	mid=(low+high)/2;
	if (arr[mid]==x){
		return mid;}
	else if (arr[mid]<x){
		if (mid+1<=high && x<=arr[mid+1]){
			return mid+1;
			}
		else{
			return binarysearch(arr,mid+1,high,x);
			}
			}
	else{
		if (mid-1>=low && x>arr[mid-1]){
			return mid;}
		else{
			return binarysearch(arr,low,mid-1,x);
		}
	}
	}
public static int zfun(int i,int index,int ki,int[] dp){
	return (index-i)*ki-(dp[i]-dp[index]);}

public static int fun(int[] arr,int n,int ki, int[] dp){
int i=binarysearch(arr,0,n-1,ki);
int temp=0;
int count;
if (i==-1){
count=0;
i=n;
}
else{
count=n-i;
}
temp=search(0,i-1,i,dp,ki);
if (temp==-1)
	return count;
return count+i-temp-1;

}

public static int search(int low,int high,int index,int[] dp,int ki){
	int mid,zmid;
	mid=(low+high)/2;
	zmid=zfun(mid,index,ki,dp);
	if (high<zfun(high,index,ki,dp)){
		return -1;}
	if (low>=zfun(low,index,ki,dp)){
		return low;}
	if (mid==zmid){
		return mid;}
	else if (mid>zmid){
		if (mid-1<=zfun(mid-1,index,ki,dp)){
			return mid;}
		else{
			return search(low,mid-1,index,dp,ki);
			}
			}
	else{
		if (mid+1>=zfun(mid+1,index,ki,dp)){
			return mid;}
		else{
			return search(mid+1,high,index,dp,ki);}
		}
	}
}

