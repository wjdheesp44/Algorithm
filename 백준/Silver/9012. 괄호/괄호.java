import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int N;
    static Deque<Character> stack;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        char[] arr;

        for (int i = 0; i < N; i++) {
            String result = "YES";
            arr = br.readLine().toCharArray();
            stack = new ArrayDeque<>();

            for (char s : arr) {
                if (s == '(') {
                    stack.push(s);
                } else if (s == ')') {
                    if (!stack.isEmpty()) stack.pop();
                    else result = "NO";
                }
            }
            if (!stack.isEmpty()) result = "NO";
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }
}