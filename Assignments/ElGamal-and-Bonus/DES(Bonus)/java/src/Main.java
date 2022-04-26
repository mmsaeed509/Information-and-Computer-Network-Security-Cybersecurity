package DES;

/**
 *
 * @author ozil
 * GitHub : https://github.com/mmsaeed509
 *
 * */

// import DES class
import DES.DES;

import javax.crypto.*;
import java.security.*;
import java.util.Scanner;

// import Libs


public class Main {

    public static void main(String[] args) {

        Scanner read = new Scanner(System.in);
        String message;

        /* Created this object to :-
        *                          - Generate secret key using DES
        *                          - initialize encryptCipher/decryptCipher
        * By Calling the constructor
        * */
        DES des = new DES();

        System.out.println("***********************");
        System.out.println("*    DES Algorithm    *");
        System.out.println("***********************");
        System.out.print("Write a message : ");
        message = read.nextLine();
        System.out.println("Encrypted message :    " + des.encrypt(message));
        System.out.println("Decrypted message :    " + des.decrypt(message));

    }
}
