import java.io.*;
import java.util.*;
public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		String ans = br.readLine();
		char[] s1 = ans.toCharArray();
		char[] s2 = br.readLine().toCharArray();
		int s = 0;
		int e = s2.length - 1;
		boolean flag = false;
		while (s1.length < e - s + 1) {
			char c = flag ? s2[s++] : s2[e--]; // 현재 방향에 맞는 끝에서 한 글자 제거
            if (c == 'B') {
                flag = !flag; // B를 제거했다면 방향 반전
            }
			
		}
		
		int N = s1.length;
		boolean same = true;
		if (!flag) {
			for (int i = 0; i < N; i++) {
				if (s2[s + i] != s1[i]) {
					same = false; break;
				}
			}
		} else {
			for (int i = 0; i < N; i++) {
				if (s2[e - i] != s1[i]) {
					same = false; break;
				}
			}
		}
		
		System.out.println(same ? 1 : 0);
	}
}