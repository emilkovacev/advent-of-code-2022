import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

import java.util.ArrayList;

class Solution {

    int max;

    static ArrayList<Integer> parse_file(String filename) {
        File data = new File(filename);

        try {
            Scanner filereader = new Scanner(data); 

            ArrayList<Integer> calories = new ArrayList<Integer>();

            while (filereader.hasNextLine()) {
                String line = filereader.nextLine();
                if (line.length() == 0) {
                    while (filereader.hasNextLine()) {
                        
                    }
                    int calorie = Integer.parseInt(line);
                    calories.add(calorie);
                }
            }

            filereader.close();
            return calories;
        } catch (FileNotFoundException e) {
            System.out.println("file not found");
            return null;
        }
    }

    static int get_max_cal(String filename) {
        ArrayList<Integer> calories = parse_file(filename);

        int max = -1;
        for (int i = 0; i < calories.size(); i++) {
            int new_cal = calories.get(i);
            if (new_cal > max) {
                max = new_cal;
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int max_cal = get_max_cal("input");
        System.out.printf("Max Calorie: %d\n", max_cal);
    }
}
