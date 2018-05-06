import java.util.*;
public class neon{
	public static void main(String[] args){
		Scanner scan=new Scanner(System.in);
		int t=scan.nextInt();
		int elem,N,i,c,stop;
		long t1,t2,total1,total2;
		while (t>0){
			t1=0;
			t2=0;
			total1=0;
			total2=0;
			c=0;
			stop=-1;
			t=t-1;
			N=scan.nextInt();
			int[] arr=new int[N];
			for (i=0;i<N;i++)
			{
				elem=scan.nextInt();
				arr[i]=elem;
				if (elem<0){
					t1=t1+elem;
				}
				else{
					t2=t2+elem;
					c=c+1;
				}				
			}
			Arrays.sort(arr);
			for (i=0;i<N;i++){
				if (arr[i]>=0)
				{
					stop=i;
					break;
				}
			}
			total1=t2*c;
			stop-=1;
			if (stop<0){
				total2=t1;
			}
			while (stop>=0){
			total1=Math.max(t2*c,(t2+arr[stop])*(c+1));
			if (t2*c<(t2+arr[stop])*(c+1))
				c=c+1;
			else
				total2=total2+arr[stop];
			stop-=1;

			}
			System.out.println(total1+total2);
		}
	}
}


