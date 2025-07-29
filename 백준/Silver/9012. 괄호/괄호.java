import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        Deque<String> stack;

        int N = Integer.parseInt(st.nextToken());
        String[] line;
        A : for (int i = 0; i < N; i++) {
            line = br.readLine().split("");
            stack = new ArrayDeque<>();

            for (String s : line) {
                if (s.equals("(")) {
                    stack.push(s);
                } else if (s.equals(")") && !stack.isEmpty()) {
                    stack.pop();
                } else {
                    sb.append("NO").append("\n");
                    continue A;
                }
            }
            if (stack.isEmpty()) sb.append("YES").append("\n");
            else sb.append("NO").append("\n");
        }
        System.out.println(sb);
    }
}