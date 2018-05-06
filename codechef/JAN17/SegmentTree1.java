import java.util.*;
import java.lang.*;
import java.io.*;
import java.lang.Math;
import java.math.*;
public class SegmentTree1 {
    private static int[] st;
//	private static int[] index;
	private static int gcd(int a, int b){
		if (b==0)
			return a;
		else
			return gcd(b,a%b);
	
	}
    static int Inverse(int a,int c){
	int y=gcd(a,c);
		if (y!=1){
			a=a/y;
			c=c/y;
			
		}
		for (int b=0;b<c;b++){
			if (a*b%c==1%c){
				return b;}
		}
	return 0;
	}
    //Construction of Segment Tree
    public static int[] constructSegmentTree(int[] arr,int P){
        int height = (int)Math.ceil(Math.log(arr.length)/Math.log(2));
        int size = 2*(int)Math.pow(2, height)-1; 
        st = new int[size];
		//index=new int[arr.length];
		//object[] arrayObjects = new object[2];
    //arrayObjects [0] = st;
    //arrayObjects [1] = index;
		
        constructST(arr, 0, arr.length-1, 0,P);
        return st;
    }
    
    public static int constructST(int[] arr, int ss, int se, int si,int P){
        if(ss==se){
            st[si] = arr[ss]%P;
			
            return st[si];
        }
        int mid = ss+(se-ss)/2;
        st[si] = constructST(arr, ss, mid, si*2+1,P)*constructST(arr, mid+1, se, si*2+2,P)%P;
        return st[si];
    }
    
    //Finding The sum of given Range
    public static int findRangeProduct(int ss, int se, int[] arr,int P){
        int n = arr.length;
        if(ss<0 || se > n-1 || ss>se){
            throw new IllegalArgumentException("Invalid arguments");
        }
        return findProduct(0, n-1, ss, se, 0,P);
    }
    
    public static int findProduct(int ss, int se, int qs, int qe, int si,int P){ 
        if(ss>qe || se < qs)return 1;
        if(qs<=ss && qe>=se)return st[si];
        
        int mid = ss+(se-ss)/2;
        return findProduct(ss, mid, qs, qe, si*2+1,P)*findProduct(mid+1, se, qs, qe, si*2+2,P)%P;
    }
    
    //Update a index value
    public static void updateValue(int arr[], int i, int newVal,int P){
        if(i<0 || i>arr.length-1)throw new IllegalArgumentException();
		//int old=arr[i];
        arr[i] = newVal;
        updValue(arr, 0, arr.length-1, i, 0, P);
    }
   private static int search(int start, int end, int i, int si)
	{
		int mid=start+(end-start)/2;
    	if (start==end){
			return si;}
else{
		if (i>mid){
			si=2*si+2;
			return search(mid+1,end,i,si);
		
		}
		if (i<=mid){
			si=2*si+1;
			return search(start,mid,i,si);
		}
}
return 0;
}
   
   
   public static void updValue(int[] arr, int ss, int se, int i, int si,int P){
	//	int P=Z;
        if(i< ss || i>se)return;
			//	int a=BigInteger.valueOf(old).modInverse(BigInteger.valueOf(P)).intValue();
        //int a=Inverse(old,P);
		/**

		if (st[si]%old!=0){
		st[si] = ((st[si]%Z)*(a))%Z;}
		else{
		st[si]=st[si]/old;
		}
		st[si]=st[si]*newVal%Z;
		**/
		int index=search(ss,se,i,si);
		st[index]=arr[i]%P;
		while (index!=0){
				
			
				index=(index-1)/2;
				st[index]=st[2*index+2]*st[2*index+1]%P;
			
			}
		
		


/**

	
		  if(ss!=se){
            int mid = ss+(se-ss)/2;
            updValue(arr, ss, mid, i, newVal, old, si*2+1,Z);
            updValue(arr, mid+1, se, i, newVal,old, si*2+2,Z);
        }
		**/
    }
	public static void square(int N, int p){
	int P=p;

//int lim=(int)Math.sqrt(N)+1;
int lim1=(int)Math.sqrt(N)+1;
if (lim1>p-1){
	lim1=p-1;
}
int f=0;
outerloop:
for (int a = 0; a <= lim1; a++)
    for (int b = 0; b <= lim1; b++)
        for (int c = 0; c <= lim1; c++)
            for (int d = 0; d <= lim1; d++)
                if ((a * a + b * b + c * c + d * d)%P == N%P){
					f=1;
                     System.out.printf("%d %d %d %d\n", a, b, c, d);
					
					break outerloop;}
if (f==0){
					System.out.println(-1);
					}
				}
    
    public static void main(String[] args) throws Exception{ 
	
			Scanner scan=new Scanner(System.in);
						BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
			int t=scan.nextInt();
				for (int i=0;i<t;i++){
					int N=scan.nextInt();
			int Q=scan.nextInt();
			int P=scan.nextInt();
	
	ArrayList<Integer> result=new ArrayList<Integer>();
			int[] arr=new int[N];
			for (int k=0;k<N;k++){
				arr[k]=scan.nextInt();
			}
			constructSegmentTree(arr,P);


				for (int j=0;j<Q;j++){
				int r=scan.nextInt();
				if (r==2){
					int m=scan.nextInt();
					int n=scan.nextInt();
					int product=findRangeProduct(m-1,n-1,arr,P);
					//System.out.println(product);
					//System.out.println("Values array = "+Arrays.toString(arr));
            //System.out.println("Segement Tree array = "+Arrays.toString(st));
			 //System.out.println("Segement Tree array = "+Arrays.toString(index));

					square(product,P);
								
				}
				else if (r==1){
					int m=scan.nextInt();
					int n=scan.nextInt();
					updateValue(arr,m-1,n,P);
				}
				}
			
				}
		    } 
}

