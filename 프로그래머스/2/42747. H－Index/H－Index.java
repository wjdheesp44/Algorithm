import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int n = citations.length;
        Arrays.sort(citations);
        
        for (int h = 0; h <= citations[n-1]; h++) {
            for (int i = 0; i < n; i++) {
                if (citations[i] >= h && n - i >= h) {
                    answer = Math.max(answer, h);
                }
            }
        }
        
        System.out.println(Arrays.toString(citations));
        
        return answer;
    }
}