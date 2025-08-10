import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static List<List<Integer>> graph;
	static boolean[] visited;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList<>();
		visited = new boolean[n+1];
		
		for (int i = 0; i <= n; i++) {
			graph.add(new ArrayList<>());
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph.get(a).add(b);
			graph.get(b).add(a);
			
		}
		
		System.out.println(bfs(1));
		
	}
	
	private static int bfs(int start) {
		Deque<int[]> q = new ArrayDeque<>();
		q.offer(new int[] {start, 0});
		visited[start] = true;
		int friendCnt = 0;
		
		while (!q.isEmpty()) {
			int[] cur = q.poll();
			int node = cur[0];
			int cnt = cur[1];
			
			for (int nd : graph.get(node)) {
				if (visited[nd] || cnt == 2) continue;
				q.offer(new int[] {nd, cnt+1});
				visited[nd] = true;
				friendCnt++;
			}
		}
		return friendCnt;
	}
}