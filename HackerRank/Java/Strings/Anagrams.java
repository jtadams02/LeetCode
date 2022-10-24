// This program determines whether or not 2 strings of any length are anagrams
// or not! :)
import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // Complete the function
        int bigger = 0;
        int smaller = 0;
        boolean aa = false;
        boolean bb = false;
        if(a.length()>=b.length())
        {
            bigger = a.length();
            smaller = b.length();
            aa = true;
        } else if(b.length()>a.length())
        {
            bigger = b.length();
            smaller = a.length();
            bb = true;
            
        }
        for(int i=0;i<bigger;i++)
        {
            char c = 'a';
            if(aa){c = Character.toUpperCase(a.charAt(i));}
            else{c = Character.toUpperCase(b.charAt(i));}
            int aCount = 0;
            int bCount = 0;
            for(int x=0;x<a.length();x++)
            {
                if(c==Character.toUpperCase(a.charAt(x))){aCount++;}
            }
            for(int y=0;y<b.length();y++)
            {
                if(c==Character.toUpperCase(b.charAt(y))){bCount++;}
            }
            if(aCount!=bCount){return false;}
        }
        /*for(int i=0;i<bigger;i++)
        {
            char tempChar = a.charAt(i);
            tempChar = Character.toUpperCase(tempChar);
            int aCount = 0;
            int bCount = 0;
            for(int k=0;k<b.length();k++)
            {
                if(Character.toUpperCase(a.charAt(k))==tempChar){aCount++;}
                if(Character.toUpperCase(b.charAt(k))==tempChar){bCount++;}
            }
            if(aCount!=bCount){return false;}
        }*/
        return true;
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}