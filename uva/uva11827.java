import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.regex.Pattern;
import java.lang.Math;
public class uva11827{
	public static void main(String[] args) throws Exception{
		Scanner scan =new Scanner(System.in);
		int t=scan.nextInt();
			//BufferedReader br = new BufferedReader(new InputStreamReader(System.in));     
        for (int p=0;p<t;p++){
				Pattern delimiters = Pattern.compile(System.getProperty("line.separator")+"|\\s");
scan.useDelimiter(delimiters);
	ArrayList<Integer> list=new ArrayList<Integer>();

while (scan.hasNextInt()){
				//String line1 =br.readLine();

			
			//String[] line=line1.split("\\s+");
			//int k=line.length;
			//for (int i=0;i<k;i++){
				//list.add(Integer.parseInt(String.valueOf(line[i])));
				list.add(scan.nextInt());
				}
			//}
			int k=list.size();
			int max_=0;
			for (int i=0;i<k;i++){
				for (int j=i+1;j<k;j++){
					max_=Math.max(max_,gcd(list.get(i),list.get(j)));
				
				}
			}
			System.out.println(max_);
		//	line1 = br.readLine();
			
			}

		}
		static int gcd(int a, int b){
		if (b==0)
			return a;
		else
			return gcd(b,a%b);
	
	}

}

