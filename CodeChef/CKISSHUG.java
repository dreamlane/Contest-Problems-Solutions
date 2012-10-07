
package codechef;
import java.io.*;
import java.math.BigInteger;
/**
 *
 * @author benjaminjohnson
 * @since  October 2012
 * 
 * solution to problem CKISSHUG on CodeChef: http://www.codechef.com/SEP12/problems/CKISSHUG
 */
public class CKISSHUG {
    public static void main(String[] args) throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

        int tests = Integer.parseInt(in.readLine());
        
        while (tests > 0)
        {
            int n = Integer.parseInt(in.readLine());
            long solution;
            int basePower;
            if (n%2 == 0) {
                basePower = (n+4)/2;}
            else {
                basePower = (n+3)/2;}
            //Now take the base power and peform modular exponentiation
            if (n%2 == 0) {
                solution = modExponent(2,basePower,1000000007) - modExponent(2,basePower-2,1000000007) - 2;
            }
            else {
                solution = modExponent(2,basePower,1000000007) - 2;
            }
            if (solution >= 0){
                out.append(String.format("%d\n", solution));
            }
            else {
                out.append(String.format("%d\n", 1000000007+solution));
            }
            tests--;
        }
        out.flush();
    }
    private static long modExponent(long base, long power, long modulo)
    {
        BigInteger number = new BigInteger(""+base);
        long solved = number.modPow(new BigInteger(""+power), new BigInteger(""+modulo)).longValue();
        //System.out.println(solved);
        return solved;
    }
}
