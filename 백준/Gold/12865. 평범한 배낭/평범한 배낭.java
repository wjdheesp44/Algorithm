import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, K, result;
    static int[][] info;
    static int[][] dp;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        info = new int[N][2];
        dp = new int[N+1][K+1];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            info[i][0] = Integer.parseInt(st.nextToken());
            info[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = N-1; i >= 0; i--) {
            for (int j = 0; j <= K; j++) {
                int b = dp[i+1][j];
                if (j + info[i][0] <= K) {
                    int a = info[i][1] + dp[i+1][j+info[i][0]];
                    dp[i][j] = Math.max(a, b);
                } else {
                    dp[i][j] = b;
                }
            }
        }
        System.out.println(dp[0][0]);
    }
}