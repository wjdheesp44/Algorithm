import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(arr);
            int cnt = 0;
            for (int i = 0; i < N; i++) {
                for (int j = i; j < N; j++) {
                    int lt = i + 1;
                    int rt = j - 1;
                    while(lt <= rt) {
                        int mid = (lt + rt) / 2;
                        int left = arr[mid] - arr[i];
                        int right = arr[j] - arr[mid];
                        if (left == right) {
                            cnt++;
                            break;
                        } else if (left < right) {
                            lt = mid + 1;
                        } else {
                            rt = mid - 1;
                        }
                    }
                }
            }
            sb.append(cnt).append("\n");
        }
        System.out.print(sb);
    }
}