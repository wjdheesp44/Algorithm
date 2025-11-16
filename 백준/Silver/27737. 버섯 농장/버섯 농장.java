import java.io.*;
import java.util.*;
public class Main {
	static int N, M, K;
	static int[][] map;
	static boolean[][] visited;
	static List<Integer> holes;
	static int[] dx = {-1, 0, 1, 0}, dy = {0, 1, 0, -1};
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		map = new int[N][N];
		visited = new boolean[N][N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
//		for (int[] a : map) System.out.println(Arrays.toString(a));
		
		holes = new ArrayList<>();
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (map[i][j] == 0 && !visited[i][j]) {
//					System.out.println(i + " " + j);
					bfs(i, j);
//					for (boolean[] a : visited) System.out.println(Arrays.toString(a));
				}
			}
		}
		
		boolean possible = true;
		int remain = M;
//		System.out.println(remain);
		for (int h : holes) {
//			System.out.println("cnt: " + h);
			if (remain < 0) possible = false;
			if (h % K != 0) {
				remain -= (h/K + 1);
//				System.out.println("hole: " + (h/K + 1));
			} else {
				remain -= (h/K);
//				System.out.println("hole: " + (h/K));
			}
//			System.out.println(remain);
		}
		
		if (possible && remain >= 0 && remain-M != 0) {
			System.out.println("POSSIBLE");
			System.out.println(remain);
		} else {
			System.out.println("IMPOSSIBLE");
		}
	}
	
	private static void bfs(int sx, int sy) {
		Deque<int[]> q = new ArrayDeque<>();
		visited[sx][sy] = true;
		q.add(new int[] {sx, sy});
		int cnt = 1;
		
		while(!q.isEmpty()) {
			int[] cur = q.poll();
			int x = cur[0]; int y = cur[1];
			
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i]; int ny = y + dy[i];
				if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
				if (map[nx][ny] == 1 || visited[nx][ny]) continue;
				q.add(new int[] {nx, ny});
				visited[nx][ny] = true;
				cnt++;
			}
		}
		holes.add(cnt);
	}
}