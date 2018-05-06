import java.util.*;
import java.lang.*;
class Codechef{
	public static void main(String[] args) throws java.lang.Exception{
		Scanner scan=new Scanner(System.in);
		int t=scan.nextInt();
		int p,q,r,i,y,x,z,flag;
		long c1,c2,c3,c4,total;
		int mod=1000000007;
		while (t>0){
			t=t-1;
			p=scan.nextInt();
			q=scan.nextInt();
			r=scan.nextInt();
			int[] A= new int[p];
			int[] B= new int[q];
			int[] C= new int[r];
			for (i=0;i<p;i++)
				A[i]=scan.nextInt();
			for (i=0;i<q;i++)
				B[i]=scan.nextInt();
			for (i=0;i<r;i++)
				C[i]=scan.nextInt();
			c1=c2=c3=c4=total=0;
			x=z=flag=0;
			Arrays.sort(A);
			Arrays.sort(B);
			Arrays.sort(C);
			long[] dpA=new long[p];
			long[] dpC=new long[r];
			dpA[0]=A[0];
			dpC[0]=C[0];
			for (i=1;i<p;i++)
				dpA[i]=(dpA[i-1]%mod+A[i]%mod)%mod;
			for (i=1;i<r;i++)
				dpC[i]=(dpC[i-1]%mod+C[i]%mod)%mod;
			
			for (i=0;i<q;i++){
				y=B[i];
			while (x<p-1){
			if (y>=A[x] && y<A[x+1]){
				break;}
			else{
				if (y<A[x]){
					flag=1;
					break;}
				if (y>=A[x+1] && y>=A[x]){
					x+=1;
					}
				}
			}
		if (flag==1){
			flag=0;
			continue;}
		while (z<r-1){
			if (y>=C[z] && y<C[z+1]){
				break;}
			else{
				if (y<C[z]){
					flag=1;
					break;}
				if (y>=C[z+1] && y>=C[z]){
					z+=1;}
					}
				}
		if (flag==1){
			flag=0;
			continue;}
		if (x==p-1){
			if (y>=A[x]){
				x=p-1;}
			else{
				x=p;}
		}
		if (z==r-1){
			if (y>=C[z]){
				z=r-1;}
			else{
				z=r;}
		}
		if (x!=p && z!=r){
			c1=(((z+1)*y)%mod*dpA[x])%mod;
			c2=((((x+1)*(z+1))%mod*(y*y)%mod)%mod+c1)%mod;
			c3=((((x+1)*y)%mod*dpC[z])%mod+c2)%mod;
			c4=((dpA[x]*dpC[z])%mod+c3)%mod;
			total=(total+c4)%mod;
			}
		else{
			break;}
			}
			System.out.println(total);

		}
		}
	}
