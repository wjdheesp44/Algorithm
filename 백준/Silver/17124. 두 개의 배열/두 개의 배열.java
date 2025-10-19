import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        
        for (int tc = 0; tc < T; tc++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int[] A = new int[n];
            int[] B = new int[m];
            long answer = 0;
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                A[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                B[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(B);
            
            for (int i = 0; i < n; i++) {
                int closeNum = B[0];
                int minDiff = Math.abs(A[i] - closeNum);
                int lt = 0;
                int rt = m-1;
                while(lt <= rt) {
                    int mid = (lt + rt) / 2;
    
                    if (A[i] == B[mid]) {
                        closeNum = B[mid];
                        break;
                    } else if (A[i] < B[mid]) {
                        rt = mid - 1;
                    } else {
                        lt = mid + 1;
                    }

                    int cal = Math.abs(A[i]-B[mid]);
                    
                    if (cal < minDiff || (cal == minDiff && B[mid] < closeNum)) {
                        minDiff = cal;
                        closeNum = B[mid];
                    }

                    
                }
                answer += closeNum;
            }
            sb.append(answer).append("\n");
        }
        System.out.println(sb);
        
    }
}