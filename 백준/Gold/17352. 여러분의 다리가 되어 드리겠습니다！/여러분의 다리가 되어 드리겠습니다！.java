import java.io.*;
import java.util.*;
public class Main {
    static int[] parent;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        parent = new int[N+1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < N-2; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            union(x, y);
        }

        int first = find(1);
        int second = -1;
        for (int i = 2; i <= N; i++) {
            if (first != find(i)) {
                second = i;
                break;
            }
        }
        System.out.println(first + " " + second);
    }

    private static int find(int a) {
        if (a == parent[a]) return a;
        return parent[a] = find(parent[a]);
    }

    private static void union(int a , int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            parent[b] = a;
        }
    }
}