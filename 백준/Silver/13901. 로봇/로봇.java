import java.io.*;
import java.util.*;
public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] map;
	static boolean[][] visited;
	static int[] dx = {0, -1, 1, 0, 0};
	static int[] dy = {0, 0, 0, -1, 1};
	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());

		map = new int[R][C];
		
		int k = Integer.parseInt(br.readLine());
		int[][] hurdle = new int[k][2];
		for (int i = 0; i < k; i++) {
			st = new StringTokenizer(br.readLine());
			hurdle[i][0] = Integer.parseInt(st.nextToken());
			hurdle[i][1] = Integer.parseInt(st.nextToken());
			map[hurdle[i][0]][hurdle[i][1]] = 1;
		}
		
		st = new StringTokenizer(br.readLine());
		int x = Integer.parseInt(st.nextToken());
		int y = Integer.parseInt(st.nextToken());
		map[x][y] = 1;
		
		st = new StringTokenizer(br.readLine());
		int[] dirs = new int[4];
		for (int i = 0; i < 4; i++) {
			dirs[i] = Integer.parseInt(st.nextToken());
		}
		int ex = x;
		int ey = y;
		while(true) {
			int cnt = 0;
			for (int i = 1; i <= 4; i++) {
				int nx = x + dx[i]; int ny = y + dy[i];
				if (nx < 0 || nx >= R || ny < 0 || ny >= C || map[nx][ny] == 1) {
					cnt++;
				}
			}
			if (cnt == 4) break;
			
			for (int i = 0; i < 4; i++) {
				
				while (true) {
					int nx = x + dx[dirs[i]];
					int ny = y + dy[dirs[i]];
					if (nx < 0 || nx >= R || ny < 0 || ny >= C) break;
					if (map[nx][ny] == 1) break;
					map[x][y] = 1;
					x = nx; y = ny;
					ex = x; ey = y;
				}
			}
		}
		System.out.println(ex + " " + ey);

	}
}