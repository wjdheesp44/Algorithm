import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[] snacks = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            snacks[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(snacks);

        long result = 0;
        long lt = 0;
        long sum = 0;
        for (int i = 0; i < N; i++) {
            sum += snacks[i];
        }
        if (sum >= M) {
            lt = 1;
        }
        
        long rt = snacks[snacks.length - 1];
        while (lt <= rt) {
            long mid = (lt + rt) / 2;
            int cnt = 0;
            for (int i = 0; i < N; i++) {
                if (mid == 0) continue;
                cnt += snacks[i] / mid;
            }
            if (cnt >= M) {
                lt = mid + 1;
                result = mid;
            } else {
                rt = mid - 1;
            }
        }

        System.out.println(result);
    }
}