// This program reverses a String!
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        String bigFatW="";
        int oppo = 0;
        for(int i=A.length()-1;i>=0;i--) 
        {
            bigFatW+=A.charAt(i);
            oppo++;
        }
        if(bigFatW.compareTo(A)==0){System.out.println("Yes");}else{System.out.println("No");}
    }
}



