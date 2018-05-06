//Segment trees
import java.lang.Math;
public class segmenttree{
	//construct a segment tree
	static void construct_tree(int input[], int segment[], int low, int high, int pos)
	{
		if (low==high)
		{
			segment[pos]=input[low];
			return;
		}
		int mid=(low+high)/2;
		construct_tree(input,segment,low,mid,2*pos+1);
		construct_tree(input,segment,mid+1,high,2*pos+2);
		segment[pos]=Math.min(segment[2*pos+1],segment[2*pos+2]);
		
	}
	//rangeminquery returns the min of input[qlow..qhigh]
	static int rangeminquery(int segtree[],int qlow, int qhigh, int low, int high, int pos)
	{
	//total overloap
	if (qlow<=low && qhigh>=high)
	{
		return segtree[pos];
	}
	//no overlap
	if (qlow>high || qhigh<low)
	{
		return Integer.MAX_VALUE;
	}
	//partial overlap, then we'll consider both right and left child of the segment tree
	int mid=(low+high)/2;
	return Math.min(rangeminquery(segtree,qlow,qhigh,low, mid,2*pos+1),rangeminquery(segtree,qlow,qhigh,mid+1,high,2*pos+2));

	}
	public static void main(String[] args)
	{
		int array[]={-1,2,4,0};
		int m=array.length;
		int n=m;
    int j=1;
//if n=2^k then p=2*n-1, else if n=k and 2^r>k then p=2^(r+1)-1
    while (n%2==0 && j>0){
			n=n/2;
			j++;

		}
    int p=(int)Math.pow(2,j+1)-1;
		
		int segment[]=new int[p];
		int max=Integer.MAX_VALUE;
		for (int i=0;i<p;i++)
		{	
			segment[i]=max;
		}

		construct_tree(array,segment,0,m-1,0);
		int k=rangeminquery(segment,1,2,0,m-1,0);
		System.out.println(k);
	}
}
