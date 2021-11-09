/*
* Name :-                                          ID :-
*
*        Mahmoud Mohamed Said Ahmed                    20180261
*
*        Omar Esmail Mohamed                           20180173
*
*        Hashem Khaled Sayed                           20180326
*
* */

package LFSR;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        int numberOfLine = 0;
        String initial = "";
        String pInitial = "";
        String ignore = "";

        try {

            File fileForStoreKey = new File("LFSR_Mahmoud-20180261_Omar-20180173_Hashem-20180326/src/LFSR/txtFiles/key.txt");
            Scanner keyFileReader = new Scanner(fileForStoreKey);

            //read form the file
            while (keyFileReader.hasNextLine()){

                if (numberOfLine==0){
                    initial = keyFileReader.nextLine();
                }else if (numberOfLine == 1){
                    pInitial = keyFileReader.nextLine();
                }else ignore = keyFileReader.nextLine();

                numberOfLine++;

            }

        } catch (FileNotFoundException e) {

            System.out.println("File Not Found");
            e.printStackTrace();

        }



    }

}
