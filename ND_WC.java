package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        String t = scanner.nextLine();
        int m = s.length();
        int n = t.length();
        int[][] S = new int[m+1][n+1];
        int max1 = 0;
        int max2 = 0;
        boolean a = false;
        boolean b = false;
        boolean c = false;
        for (int i = 0; i < m+1; i++) {
            for (int j = 0; j < n+1; j++) {
                S[i][j] = Integer.MIN_VALUE;
            }
        }
        S[0][0] = 0;
        for (int i = 1; i < m+1; i++) {
            S[i][0] = S[i-1][0] + 1; //gap penalty
        }
        for (int j = 1; j < n+1; j++) {
            S[0][j] = S[0][j-1] + 1; //gap penalty
        }
        for (int i = 1; i < m+1; i++) {
            for (int j = 1; j < n+1; j++) {
                if (isSame(s.charAt(i-1),t.charAt(j-1)))
                    S[i][j] = S[i-1][j-1];
                else
                    S[i][j] = Math.min( S[i-1][j-1] ,Math.min( S[i-1][j] , S[i][j-1])) +1;
            }
        }
        System.out.println(S[m][n]);
    }
    public static boolean isSame(char a, char b){
        return (a==b);
    }
}
