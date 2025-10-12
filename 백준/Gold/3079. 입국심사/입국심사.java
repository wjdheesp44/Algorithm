import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long N = Integer.parseInt(st.nextToken());
        long M = Integer.parseInt(st.nextToken());

        ArrayList<Integer> times = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int a = Integer.parseInt(br.readLine());
            times.add(a);
        }
        times.sort(null);
        long result = (long)(Math.pow(10, 9)*M)/N;
        long lt = M/N; long rt = (long)(Math.pow(10, 9)*M)/N;

        while (lt <= rt) {
            long mid = (lt + rt) / 2;
            long total = 0;
            long cnt = 0;
            for (int time : times) {
                cnt += mid / time;
            }
            if (cnt < M) {
                lt = mid + 1;
            } else {
                result = Math.min(mid, result);
                rt = mid - 1;
            }
        }
        System.out.println(result);
    }
}