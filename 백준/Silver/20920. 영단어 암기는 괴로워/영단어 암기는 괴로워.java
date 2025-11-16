import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		HashMap<String, Integer> map = new HashMap<>();
		Set<String> set = new HashSet<>();
		for (int i = 0; i < N; i++) {
			String word = br.readLine();
			if (word.length() >= M) {
				map.put(word, map.getOrDefault(word, 0) + 1);
				set.add(word);
			}
		}
		
		List<String> words = new ArrayList<>(set);
		words.sort((a, b) -> {
			int aCnt = map.get(a); int bCnt = map.get(b);
			if (aCnt != bCnt) {
				return Integer.compare(bCnt, aCnt);
			} else if (a.length() != b.length()) {
				return Integer.compare(b.length(), a.length());
			} else {
				return a.compareTo(b);
			}
		});
		
		for (String word : words) {
			sb.append(word).append("\n");
		}
		System.out.println(sb);
	}
}