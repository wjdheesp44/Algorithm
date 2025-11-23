import java.io.*;
import java.util.*;
public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[] parents;
	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		parents = new int[n];
		
		for (int i = 0; i < n; i++) {
			parents[i] = i;
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			if (find(a) == find(b)) {
				System.out.println(i+1);
				System.exit(0);
			}
			union(a, b);
		}
		System.out.println(0);
	}
	
	private static void union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a != b) {
			parents[b] = a;
		}
	}
	
	private static int find(int a) {
		if (parents[a] == a) return a;
		return parents[a] = find(parents[a]);
	}
}