//import java.util.scanner;
import java.util.*;
import java.lang.*;
import java.io.*;
public class uva10407{
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));     
        String line1 =br.readLine();
		ArrayList<Integer> result=new ArrayList<Integer>();
		while(line1.length()>1){
			ArrayList<Integer> list=new ArrayList<Integer>();
			String[] line=line1.split("\\s+");
			int k=line.length;
			for (int i=0;i<k-1;i++){
				list.add(Integer.parseInt(String.valueOf(line[i])));
			}
			for (int i=1;i<k-1;i++){
				list.set(i,list.get(i)-list.get(0));
			}
			int res=gcd_multiple(list);
			result.add(res);
            //System.out.println(res);
            line1 = br.readLine();
        }
		for (int p:result)
			System.out.println(p);
	}
	static int gcd(int a, int b){
		if (b==0)
			return a;
		else
			return gcd(b,a%b);
	
	}
	static int gcd_multiple(ArrayList<Integer> list){
		int k=list.size();
		if (k==1){
			return list.get(0);}
		else if (k==2){
			return gcd(list.get(0),list.get(1));}
		else{
		int result=list.get(1);
		for (int i=2;i<list.size();i++)
			result=gcd(result,list.get(i));
		if (result==0)
			return list.get(0);
		else
			return result;
		}
	
	}
}

	
			
