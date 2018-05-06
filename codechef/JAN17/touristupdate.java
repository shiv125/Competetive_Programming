import java.io.*;
import java.util.*;
import java.lang.*;
import java.util.LinkedList;


class Graph{
	private int V;
	private LinkedList<Integer> adj[];

	Graph(int v)
	{
		V=v;
		adj=new LinkedList[v];
		for (int i=0;i<v;++i)
			adj[i]=new LinkedList<Integer>();
	
	}

	void addEdge(int u, int v)
	{
		adj[u].add(v);
		adj[v].add(u);
	}
	void DFS(int v, boolean visited[])
	{
		visited[v]=true;
		Iterator<Integer> i=adj[v].listIterator();
		while (i.hasNext())
		{
			int n=i.next();
			if (!visited[n])
				DFS(n,visited);
		
		
		}
	
	}
	boolean isConnected()
    {
        // Mark all the vertices as not visited
        boolean visited[] = new boolean[V];
        int i;
        for (i = 0; i < V; i++)
            visited[i] = false;
 
        // Find a vertex with non-zero degree
        for (i = 0; i < V; i++)
            if (adj[i].size() == 0)
                return false;
		for (i = 0; i < V; i++)
            if (adj[i].size() != 0)
                break;
 
        // If there are no edges in the graph, return true
        if (i == V)
            return true;
 
        // Start DFS traversal from a vertex with non-zero degree
        DFS(i, visited);
 
        // Check if all non-zero degree vertices are visited
        for (i = 0; i < V; i++)
           if (visited[i] == false && adj[i].size() > 0)
                return false;
 
        return true;
    }

	boolean isEulerian()
    {
        // Check if all non-zero degree vertices are connected
        if (isConnected() == false)
            return false;
 
              int odd = 0;
		int k=0;
        for (int i = 0; i < V; i++){
            if (adj[i].size()%2!=0){
                odd++;
				}
			if (adj[i].size()==0){
				return false;
			}
 }
        // If count is more than 2, then graph is not Eulerian
        if (odd >0)
            return false;
        return true;
    }
	//efficient algorithm
	void efficient(List<Integer> res){
		Stack<Integer> st=new Stack<Integer>();
	int current=0;
	st.push(current);
	int c=0;
	int x;
	//List<Integer> res= new ArrayList<Integer>();
	while(!st.empty()){
		
		while (adj[current].size()!=0){
			Iterator<Integer> i=adj[current].listIterator();
		while (i.hasNext())
		{
			int u=i.next();
			st.push(current);
			removeEdge(current,u);
			current=u;
			break;			
			
		}
		}
		
			
		res.add(current);
	//System.out.printf("%d ",current+1);
		current=st.pop();
		}
	}


		void removeEdge(int u, int v)
	{
				adj[v].remove(Integer.valueOf(u));
			adj[u].remove(Integer.valueOf(v));
	}
}

	public class touristupdate{

	static int hashcode(int a,int b){
	int hash;
	
	
	int sum = a+b;
    hash = sum * (sum+1)/2 + a;
	return hash;
  }
	
	
	
	
	public static void main(String args[])
    {
        // Let us create and test graphs shown in above figures
		Scanner scan=new Scanner(System.in);
		int V=scan.nextInt();
		int E=scan.nextInt();
        Graph g = new Graph(V);
		int c,d;
		int m,n;
      	int[][] arrays=new int[E][2];
		int[][] arr=new int[E][2];
		//int[] final_=new int[E];
		HashMap<Integer, Boolean> map = new HashMap<Integer, Boolean>();
		//HashMap<Integer, Map<Integer, Boolean>> map=new HashMap<Integer,Map<Integer,Boolean>>();
		int pr;
		int counter=0;
		for (int i=0;i<E;i++)
		{
			int a=scan.nextInt()-1;
			int b=scan.nextInt()-1;
			arrays[i][0]=a;

			arr[i][0]=0;
			arr[i][1]=0;
			
			arrays[i][1]=b;
			//int[] data=new int[]{a,b};
			//int[] data1=new int[]{b,a};
			//map.put(data,false);
			//map.put(data1,false);
			//map.put(a,b);
			//map.put(b,a);
			//map.put(map.get())
		m=hashcode(a,b);
		n=hashcode(b,a);
		map.put(m,true);
		map.put(n,false);
			g.addEdge(a,b);
			
		}	
		//pr=arrays[0][]
	
			if (g.isEulerian()){
			System.out.println("YES");
			List<Integer> res=new ArrayList<Integer>();
			g.efficient(res);
			for (int i=0;i<res.size()-1;i++){
				arr[i][0]=res.get(res.size()-i-1);
				arr[i][1]=res.get(res.size()-i-2);
				//System.out.print(res.get(2));
				}
			
			for (int i=0;i<E;i++)
			{
				int data=hashcode(arr[i][0],arr[i][1]);
				int data1=hashcode(arr[i][1],arr[i][0]);
				if (map.get(data)==false){
					counter+=1;
					map.put(data,true);
					map.put(data1,false);
				}
				
				//System.out.println(map.get(data));
				}
				//System.out.println(Arrays.asList(map));
		//	if (counter>E/2){
			
		//	}
		if (counter<=E/2){
			for (int i=0;i<E;i++)
			{
				c=arrays[i][0];
				d=arrays[i][1];

				int data=hashcode(c,d);
				c=c+1;
				d=d+1;
				
				if (map.get(data)==true)
					System.out.printf("%d %d\n",c,d);
				else
					System.out.printf("%d %d\n",d,c);
			}
			}
			else{
			for (int i=0;i<E;i++)
			{
				c=arrays[i][0];
				d=arrays[i][1];

				int data=hashcode(c,d);
				c=c+1;
				d=d+1;
				
				if (map.get(data)==true)
					System.out.printf("%d %d\n",d,c);
				else
					System.out.printf("%d %d\n",c,d);
			}

			
			
			
			
			}
			
			
			
			
			

			}
			/**
				
				for (int j=0;j<E;j++){
					if ((arr[j][0]==arrays[i][0]) && (arr[j][1]==arrays[i][1])){
						final_[i]=1;
						break outerloop;
					}
					else if ((arr[j][0]==arrays[i][1]) && (arr[j][1]==arrays[i][0])){
						final_[i]=-1;
						break outerloop;
				}
				
				}
			
			
			for (int k=0;k<E;k++){
				c=arrays[k][0]+1;
				d=arrays[k][1]+1;
				if (final_[k]==1){
					System.out.printf("%d %d\n",c,d);
					
				}
				else{
					System.out.printf("%d %d\n",d,c);
				}
			
			}
			**/
			
		else{
			System.out.println("NO");
			}

        
		}
}



