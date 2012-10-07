
import java.io.*;
import java.util.*;
/**
 *
 * @author benjaminjohnson
 * @since September 2012
 * 
 * solution to code chef problem: http://www.codechef.com/SEP12/problems/HORSES
 */
public class HORSES {
    public static void main(String[] args) throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int T = Integer.parseInt(in.readLine());
        
        while ( T > 0)
        {
            in.readLine();
            //Get the data into an arrayList
            ArrayList<Integer> horses = new ArrayList<Integer>();
            String[] inputLine = in.readLine().split(" ");
            for (String horse : inputLine)
            {
                horses.add(Integer.parseInt(horse));
            }
            Collections.sort(horses);
            
            //now check diffs
            int minDiff = Integer.MAX_VALUE;
            for (int i = 1; i < horses.size(); i++)
            {
                if (horses.get(i) - horses.get(i-1) < minDiff)
                {
                    minDiff = horses.get(i)-horses.get(i-1);
                }
            }
            out.append(String.format("%d\n", minDiff));
            T--;
        }
        out.flush();
    }
}
