import java.util.*;

import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();

        

        HashMap<Integer, String> hash = new HashMap<>();

        hash.put(1, "one");

        hash.put(2, "two");

        hash.put(3, "three");

        hash.put(4, "four");

        hash.put(5, "five");

        hash.put(6, "six");

        hash.put(7, "seven");

        hash.put(8, "eight");

        hash.put(9, "nine");

        hash.put(0, "zero");

        

        int M = Integer.parseInt(st.nextToken());

        int N = Integer.parseInt(st.nextToken());

        

        ArrayList<String> arr = new ArrayList<>();

        HashMap<String, Integer> hash2 = new HashMap<>();

        for (int i = M; i <= N; i++) {

            if (i < 10) {

                arr.add(hash.get(i));

                hash2.put(hash.get(i), i);

            } else {

                int a = i / 10;

                int b = i % 10;

                String temp = hash.get(a) + hash.get(b);

                arr.add(temp);

                hash2.put(temp, i);

            }

        }

        

        arr.sort(null);

        

        int cnt = 0;

        for (String a : arr) {

            if (cnt >= 10) {

                cnt = 0;

                sb.append("\n");

            }

            sb.append(hash2.get(a)).append(" ");

            cnt++;

        }

        System.out.println(sb);

    }

}