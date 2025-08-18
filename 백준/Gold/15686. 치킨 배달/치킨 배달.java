import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int N, M;
    static boolean[][] visited;
    static int[][] map;
    static ArrayList<int[]> chickens;
    static ArrayList<int[]> houses;
    static int[] selected;
    static int result;

    // 치킨집 M개를 뽑고(조합), 한 집에서 치킨집들 간의 dist를 구해서 최솟값 갱신해서 총합 구하기
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][N];
        chickens = new ArrayList<>();
        houses = new ArrayList<>();
        result = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 2) {
                    chickens.add(new int[]{i, j});
                } else if (map[i][j] == 1) {
                    houses.add(new int[]{i, j});
                }
            }
        }

        combination(0, 0, new int[M]);
        System.out.println(result);


    }

    private static void combination(int depth, int chickenHouseCnt, int[] selected) {
        if (chickenHouseCnt == M) {
            result = Math.min(result, calDist(selected));
            return;
        }
        if (depth >= chickens.size()) return;

        selected[chickenHouseCnt] = depth;
        combination(depth + 1, chickenHouseCnt+1, selected);
        combination(depth + 1, chickenHouseCnt, selected);
    }

    private static int calDist(int[] selected) {
        int total = 0;
        for (int[] cur : houses) {
            int houseDist = Integer.MAX_VALUE;
            int hx = cur[0]; int hy = cur[1];
            for (int k = 0; k < M; k++) {
                houseDist = Math.min(houseDist, Math.abs(chickens.get(selected[k])[0] - hx) + Math.abs(chickens.get(selected[k])[1] - hy));
            }
            total += houseDist;
        }
        return total;
    }
}