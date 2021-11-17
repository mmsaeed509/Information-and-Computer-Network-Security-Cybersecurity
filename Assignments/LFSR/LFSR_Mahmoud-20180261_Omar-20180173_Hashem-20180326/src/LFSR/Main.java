/**
*
* Name :-                                          ID :-
*
*         Mahmoud Mohamed Said Ahmed                    20180261
*
*         Omar Esmail Mohamed                           20180173
*
*         Hashem Khaled Sayed                           20180326
*
**/

package LFSR;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        List<Integer> sInitial = new ArrayList<>();     // Initial Key
        List<Integer> pGate = new ArrayList<>();        // Gates
        List<Integer> newKey = new ArrayList<>();       // New Key
        List<Integer> planText = new ArrayList<>();      // Store Plan Text
        List<Integer> encryptedPlanText = new ArrayList<Integer>();     // Store Encrypted Plan Text

        String patternKeyChecker = "";       // Prevent Repetition In Key
        String initialKey  = "";   // Initial Key
        String pInitialGates = "";   // Gates
        String IgnoreBits   = "";   // Bits We Will Ignore Form The Key
        String Key = "";    // Key
        String PlanText = "";   // Plan Text

        int numberOfLineInKeyFile = 0;// Number Of Lines We Will read Key & Gates & Ignore Bits


        try {

            File fileForStoreKey = new File("src/LFSR/txtFiles/key.txt");
            Scanner keyFileReader = new Scanner(fileForStoreKey);

            //read form the file
            while (keyFileReader.hasNextLine()){

                if (numberOfLineInKeyFile==0){
                    // Initial Key
                    initialKey = keyFileReader.nextLine();
                }else if (numberOfLineInKeyFile == 1){
                    // Gates
                    pInitialGates = keyFileReader.nextLine();
                }else{
                    // Bits We Will Ignore Form The Key
                    IgnoreBits = keyFileReader.nextLine();
                }

                numberOfLineInKeyFile++;

            }

            // Read The Initial Key From The File And Store It In The List Key
            for (int i = 0; i <initialKey.length() ; i++) {

                sInitial.add(Integer.parseInt(initialKey.charAt(i)+""));

            }

            // Read The Initial Gates From The File And Store It In The List Gates
            for (int i = 0; i < pInitialGates.length(); i++) {

                pGate.add(Integer.parseInt(pInitialGates.charAt(i)+""));
                
            }

            keyFileReader.close();

        } catch (FileNotFoundException e) {

            System.out.println("File Not Found");
            e.printStackTrace();

        }

        Key+=initialKey;
        patternKeyChecker = Key ;

        int index = 0;
        boolean testPatternRepeated = false ; // If Pattern Repeated testPatternRepeated = true & stop Generating The Key
        String repeatedPatternKeyInLoop = ""; // Check The Pattern Is Repeated Or Not

        while (Key.length()<511 &!testPatternRepeated){

            // Adding The New Bit At The End
            Key+= pGate.get(0)*sInitial.get(0+index)^pGate.get(1)*sInitial.get(1+index)^pGate.get(2)*sInitial.get(2+index)^pGate.get(3)*sInitial.get(3+index)^pGate.get(4)*sInitial.get(4+index)^pGate.get(5)*sInitial.get(5+index)^pGate.get(6)*sInitial.get(6+index)^pGate.get(7)*sInitial.get(7+index)^pGate.get(8)*sInitial.get(8+index);

            // Getting The Last Bit And Add It To The List Key
            sInitial.add(Integer.parseInt(Key.charAt(Key.length()-1)+""));

            // Preventing Pattern Key Repetition
            repeatedPatternKeyInLoop=Key.substring(Key.length()-9,Key.length());

            // If patternKeyChecker = repeatedPatternKeyInLoop That Means There Are Repeating In Pattern Key Generation , testPatternRepeated = true , Stop Generating The Key
            testPatternRepeated=patternKeyChecker.contains(repeatedPatternKeyInLoop);

            index++;
            patternKeyChecker = repeatedPatternKeyInLoop;

        }

        // Printing The Pure Key
        System.out.println("The Pure Key Is : " + initialKey + "    And It's Size Is : " + initialKey.length());

        // Printing The Key After Adding Bits
        System.out.println("The Key After Adding Bits Is : " + Key + "    And It's Size Is : " + Key.length());

        int ignoreNumber = Integer.parseInt(IgnoreBits);

        // Ignore The Bits From The Front
        for (int i = ignoreNumber; i <Key.length() ; i++) {

            newKey.add(Integer.parseInt(Key.charAt(i)+""));

        }

        System.out.println("No. Ignores Bits Is : " + ignoreNumber );

        System.out.println("The New Key Is : " + newKey + "    And It's Size Is : " + newKey.size());


        try {

            File fileForPlanText = new File("src/LFSR/txtFiles/PlanText.txt");
            Scanner planTextReader = new Scanner(fileForPlanText);

            // Read The Plan Text From The File
            while (planTextReader.hasNextLine()){

                PlanText+= planTextReader.nextLine();

            }

            planTextReader.close();

        } catch (FileNotFoundException e) {

            System.out.println("File Not Found");
            e.printStackTrace();

        }

        //Adding Plant Text To List planText
        for (int i = 0; i <PlanText.length() ; i++) {

            planText.add(Integer.parseInt(PlanText.charAt(i)+""));

        }

        //Printing Plan Text
        System.out.println("Plan Text : " + PlanText + "    And It's Size IS : " + PlanText.length());

        // Encryption

        // PlanTextCounter, Because Plan Text Size != newKey Size
        int plantTextCounter = 0;
        /*
        *
        * Plan Text = 0101100101 ==> 10 Bits
        * New Key   = 01011001   ==> 8  Bits
        * PlanText XOR NewKey ==> There Are 2 Bits Will Remain From The Plan Text
        * 2 Bits Remaining Form PlanText XOR The First 2 Bit From NewKey
        * We Need plantTextCounter To Stop The XOR Operation
        *
        * */

        while (planText.size()!=encryptedPlanText.size()){

            for (int i = 0; i < newKey.size() ; i++) {

                encryptedPlanText.add(newKey.get(i)^planText.get(plantTextCounter));
                plantTextCounter++;

                // Her We Stop The XOR Operation As We Mentioned Before
                if (plantTextCounter==planText.size())break;

            }

        }

        System.out.println("The Encrypted Plan Text : " + encryptedPlanText + "   And It's Size : " + encryptedPlanText.size());


        // Decryption

        String decryptedPlaneText = "";

        // decryptedPlaneTextCounter as same as plantTextCounter
        int decryptedPlaneTextCounter = 0;

        while (encryptedPlanText.size()!=decryptedPlaneText.length()){

            for (int i = 0; i < newKey.size(); i++) {

                decryptedPlaneText +=newKey.get(i)^encryptedPlanText.get(decryptedPlaneTextCounter);
                decryptedPlaneTextCounter++;

                if (decryptedPlaneTextCounter == encryptedPlanText.size())break;

            }

        }

        System.out.println("Plan Text After Decryption : " + decryptedPlaneText + "   And It's Size : " + decryptedPlaneText.length());

    }
}
