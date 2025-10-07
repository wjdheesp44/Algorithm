import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int lt = 1;
        int rt = 0;
        int result = 0;
        
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            rt = Math.max(rt, arr[i]);
        }
        int M = Integer.parseInt(br.readLine());
        
        while (lt <= rt) {
            int mid = (lt + rt) / 2;

            int total = 0;
            for (int i = 0; i < N; i++) {
                if (arr[i] <= mid) {
                    total += arr[i];
                } else total += mid;
            }

            if (total <= M) {
                result = mid;
                lt = mid + 1;
            } else {
                rt = mid - 1;
            }
            
        }

        System.out.println(result);
        
    }
}