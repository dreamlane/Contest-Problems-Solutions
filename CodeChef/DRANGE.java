
import java.io.*;
/**
 *
 * @author benjaminjohnson
 * @since August 2012
 * 
 * solution to code chef problem: http://www.codechef.com/problems/TWTCLOSE
 */
public class DRANGE {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException{
        
        //Get input
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] inputLine = in.readLine().split(" ");
        int N = Integer.parseInt(inputLine[0]);
        int K = Integer.parseInt(inputLine[1]);
        boolean[] tweets = new boolean[N]; //if false then closed
        int open = 0;
        
        for (int i = 0; i < K; i++)
        {
            String input = in.readLine();
            if (input.contains("CLOSEALL"))
            {
                tweets = new boolean[N];
                open = 0;
            }
            else
            {
                //get the tweet number
                int tweetNumber = Integer.parseInt(input.split(" ")[1]);
                //check to see if the tweet is open or closed
                if (tweets[tweetNumber-1])
                {
                    tweets[tweetNumber-1] = false;
                    open--;
                }
                else
                {
                    tweets[tweetNumber-1] = true;
                    open++;
                }
            }
            out.append(String.format("%d\n", open));
        }
        out.flush();
    }
}
