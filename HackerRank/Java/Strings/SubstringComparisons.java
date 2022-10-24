// This program compares 2 strings and
// determines the largest and smallest 
// lexographical substrings
import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        for(int i=0;i<s.length();i++)
        {
            if(i+k>s.length()){continue;}else{
               String sub = s.substring(i, i+k);
               if(i==0){smallest=sub;largest=sub;continue;}
               if(sub.compareTo(largest)>0){largest=sub;}
               if(sub.compareTo(smallest)<0){smallest=sub;} 
            }
        }
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}