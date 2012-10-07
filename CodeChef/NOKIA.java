
import java.io.*;

/**
 *
 * @author benjaminjohnson
 * @since August 2012
 * 
 * solution to code chef problem: http://www.codechef.com/problems/NOKIA
 */
public class NOKIA {
    public static void main(String[] args) throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        
        int tests = Integer.parseInt(in.readLine());
        
        while (tests > 0)
        {
            String[] inLine = in.readLine().split(" ");
            int N = Integer.parseInt(inLine[0]);
            int M = Integer.parseInt(inLine[1]);
            
            if (N == 1)
            {
                if (M < 2)
                {
                    System.out.println(String.format("%d", -1));
                }
                else
                {
                    System.out.println(String.format("%d",M-2));
                }
            }
            else if (N == 2)
            {
                if (M < 5)
                {
                    System.out.println(String.format("%d", -1));
                }
                else
                {
                    System.out.println(String.format("%d",M-5));
                }
            }
            else
            {
                //find the shortest length of wire for N
                int[] mins = {0,2,5,8,12,16,20,24,29,34,39,44,49,54,59,64,70,76
                        ,82,88,94,100,106,112,118,124,130,136,142,148,154};
                //the maximum is the sum of digits from 2 to N+1
                int maximum = 0;
                for (int i = 2; i <= N+1; i++){
                    maximum += i;}
                //the solution is -1 if M < minumum
                if (M < mins[N]){
                    System.out.println(String.format("%d", -1));
                }
                //if M is less than or equal to maximum, then the solution is 0
                else if (M <= maximum){
                    System.out.println(String.format("%d", 0));
                }
                else {
                    System.out.println(String.format("%d",M-maximum));
                }
            }
            tests--;
        }
    }
}
