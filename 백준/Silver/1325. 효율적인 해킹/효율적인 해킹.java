import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int N, M;
	static List<List<Integer>> graph;
	static int maxHacking;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList<>();
		
		for (int i = 0; i <= N; i++) {
			graph.add(new ArrayList<>());
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph.get(b).add(a);
			
		}
		
		List<Integer> result = new ArrayList<>();
		for (int i = 1; i <= N; i++) {
			int curCnt = bfs(i);
			if (maxHacking == curCnt) {
				result.add(i);
			} else if (maxHacking < curCnt) {
				maxHacking = curCnt;
				result.clear();
				result.add(i);
			}
		}
		result.sort((a, b) -> a - b);

		for (int i : result) {
			sb.append(i).append(" ");
		}
		System.out.println(sb);
	}
	
	private static int bfs(int start) {
		boolean[] visited = new boolean[N+1];
		Deque<Integer> q = new ArrayDeque<>();
		q.offer(start);
		visited[start] = true;
		int cnt = 0;
		
		while (!q.isEmpty()) {
			int node = q.poll();
			for (int n : graph.get(node)) {
				if (visited[n]) continue;
				q.offer(n);
				visited[n] = true;
				cnt++;
			}
		}
		return cnt;	
	}
}