import java.io.*;
import java.util.*;
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int H, W;
    static char[][] map;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    public static void main(String[] args) throws Exception{
        st = new StringTokenizer(br.readLine());
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());

        map = new char[H][W];
        for (int i = 0; i < H; i++) {
            String line = br.readLine();
            for (int j = 0; j < W; j++) {
                map[i][j] = line.charAt(j);
            }
        }

        int result = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (map[i][j] == 'W') continue;
                result = Math.max(bfs(i, j), result);
            }
        }
        System.out.println(result);
    }

    private static int bfs(int sx, int sy) {
        Deque<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[H][W];
        q.offer(new int[]{sx, sy, 0});
        visited[sx][sy] = true;
        int max = 0;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0]; int y = cur[1]; int cnt = cur[2];
            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i]; int ny = y + dy[i];
                if (nx < 0 || ny < 0 || nx >= H || ny >= W) continue;
                if (visited[nx][ny] || map[nx][ny] == 'W') continue;
                visited[nx][ny] = true;
                q.offer(new int[]{nx, ny, cnt+1});
                max = Math.max(max, cnt+1);
            }
        }
        return max;
    }
}