import java.util.*;
import java.io.*;
import java.lang.Math;
public class uva787{
	public static void main(String[] args)
	{
		Scanner scan=new Scanner(System.in);
	
		String inp;
		int c,i,y,curr_max_prod,curr_min_prod,max_prod,zero,min_prod;
		zero=-1;
		ArrayList<Integer> result=new ArrayList<Integer>();
		int j=0;
		
		  while(scan.hasNextInt()){
		  /**
		  	
			String[] str=inp.split("\\s");
			int len=(str.length)-1;
			int[] t=new int[len];
			c=0;
			for (String x:str){
				y=Integer.parseInt(x);
				if (y!=-999999){
					t[c]=y;
					c+=1;}
			}**/
			while ((n=scan.nextInt())!=-999999){
				
			}

			//System.out.println(t[0]);
				curr_max_prod=t[0];
		max_prod=t[0];
		curr_min_prod=t[0];
		min_prod=t[0];
		if (t[0]==0){
			zero=1;
		}
		
			for (i=1;i<len;i++){
				if (t[i]==0){
					zero=1;}
					curr_max_prod=Math.max(curr_max_prod*t[i],t[i]);
			
			if (curr_min_prod<0){
				if (t[i]<0){
					curr_max_prod=Math.max(curr_min_prod*t[i],curr_max_prod);}
			curr_min_prod=Math.min(curr_min_prod*t[i],t[i]);
			
			}

			if (max_prod<curr_max_prod){
				max_prod=curr_max_prod;}
				}
		if (max_prod<0){
			if (zero==1){
				max_prod=0;
				}
			}
					
			//System.out.println(max_prod);
			result.add(max_prod);


		}
		for (int r:result){
			System.out.println(r);
		
		}
		//System.out.println(t);
		
	}
	}

