import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int N, M;
    static int[] inDegree;
    static ArrayList<ArrayList<Integer>> graph;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        inDegree = new int[N+1];
        int[] result = new int[N+1];
        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            inDegree[b]++;
        }

        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            result[i] = 1;
            if (inDegree[i] == 0) {
                q.offer(i);
            }
        }
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int next : graph.get(cur)) {
                result[next] = result[cur]+1;
                inDegree[next]--;
                if (inDegree[next] == 0) {
                    q.offer(next);
                }
            }
        }
        for (int i = 1; i < N+1; i++) {
            sb.append(result[i]).append(" ");
        }
        System.out.println(sb);
    }
}