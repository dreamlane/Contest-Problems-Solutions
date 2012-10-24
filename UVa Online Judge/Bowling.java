
import java.util.Arrays;
import java.io.*;
import sun.reflect.generics.tree.IntSignature;

/**
 *
 * @author benjaminjohnson
 */
public class Bowling {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)throws IOException{
        // TODO code application logic here
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String line = in.readLine();
        //int cases = 0;
        while (!line.equals("Game Over")) {
            //cases++;
            /*
            if (cases > 50000) {
                break;
            }*/
            int frames = 0;
            int bowls = 0;
            boolean strike = false;
            boolean spare = false;
            String[] ins = line.split(" ");
            int[] scores = new int[ins.length];
            //System.out.println(Arrays.toString(ins));
            for (int i =0; i < ins.length;i++) {
                if (frames <10){
                    //System.out.println("frames: "+frames+" bowls: "+bowls+" result: "+ins[i]);
                    if (ins[i].contains("X")) {
                        frames++;
                        bowls = 0;
                        scores[i] = -2;
                        if (frames == 10){
                            strike = true;
                        }
                    }
                    else if (ins[i].contains("/")) {
                        frames++;
                        bowls = 0;
                        scores[i] = -1;
                        if (frames == 10) {
                            spare = true;
                        }
                    }
                    else {
                        if (bowls == 1) {
                            bowls = 0;
                            frames++;
                        }
                        
                        else{bowls++;}
                        scores[i] = Integer.parseInt(ins[i]);
                    }
                }
                else if (bowls < 2){
                    //System.out.println("frames: "+frames+" bowls: "+bowls+" result: "+ins[i]);
                    if (strike){
                        if (ins[i].equals("X")){
                            scores[i] = -2;
                        }
                        else if (ins[i].equals("/")) {
                            scores[i] = -1;
                        }
                        else {
                            scores[i] = Integer.parseInt(ins[i]);
                        }
                    }
                    else if (bowls < 1) {
                        if (ins[i].equals("X")){
                            scores[i] = -2;
                        }
                        else if (ins[i].equals("/")) {
                            scores[i] = -1;
                        }
                        else {
                            scores[i] = Integer.parseInt(ins[i]);
                        }
                    }
                    bowls++;
                }
            }
            //System.out.println(Arrays.toString(scores));
            int sum = 0;
            try {
                for (int i = 0; i < ins.length;i++ ){
                    if (scores[i]==-2) {
                        scores[i] = 10;
                        if (scores[i+1] == -2) {
                            scores[i] += 10;
                        }
                        else {
                            scores[i] += scores[i+1];
                        }
                        if (scores[i+2]==-2) {
                            scores[i] += 10;
                        }
                        else if (scores[i+2]==-1) {
                            scores[i] += 10;
                            scores[i] -= scores[i+1];
                        }
                        else {
                            scores[i] += scores[i+2];
                        }
                    }
                    else if (scores[i] == -1) {
                            scores[i-1] = 0;
                            scores[i] = 10;
                            //System.out.println("after spare "+ ins[i+1]);
                        if (scores[i+1] == -2) {
                            scores[i] += 10;
                        }
                        else {
                            scores[i] += scores[i+1];
                        }
                    }
                }
            }catch(Exception e) {}
            int offset = strike ? 2:0;
            offset = spare ? 1:offset;
            //System.out.println(Arrays.toString(scores));
            //System.out.println(offset);
           for (int i = 0; i < scores.length-offset;i++) {
               sum+= scores[i];
           }
           out.append(""+sum+"\n");
           line = in.readLine();
        }
        out.flush();
    }
}
