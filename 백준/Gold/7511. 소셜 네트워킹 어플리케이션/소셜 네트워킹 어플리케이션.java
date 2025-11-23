import java.util.*;
import java.io.*;
public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int[] parents;
	
	public static void main(String[] args) throws Exception {
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(br.readLine());
			
			parents = new int[N];
			for (int i = 0; i < N; i++) {
				parents[i] = i;
			}
			
			int K = Integer.parseInt(br.readLine());
			
			for (int i = 0; i < K; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				union(a, b);
			}

			int P = Integer.parseInt(br.readLine());

			sb.append("Scenario ").append(tc).append(":").append("\n");
			for (int i = 0; i < P; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				if (find(a) == find(b)) {
					sb.append(1).append("\n");
				} else {
					sb.append(0).append("\n");
				}
			}
			sb.append("\n");
		}
		System.out.println(sb);
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