package DS;

import java.io.UnsupportedEncodingException;
import java.security.*;
import java.util.*;

/**
 *
 * @author Omar Esmail
 * GitHub : https://github.com/OmarEsmail211
 *
 * @contributor Ozil
 * GitHub : https://github.com/mmsaeed509
 *
 * Omar Esmail Mohamed 				20180173
 * Mahmoud Mohamed Saied			20180261
 * Abdallah Adham Sharkawy			20180161
 *
 */


public class Main {

    public static void main(String[] args) throws Exception {

        /* Read Text */
        Scanner readText = new Scanner(System.in);
        System.out.print("Enter text : ");
        String text = readText.nextLine();

        /* Creating KeyPair generator object */
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("DSA");

        /* Initializing the key pair generator */
        keyPairGenerator.initialize(2048);

        /* Generate the pair of keys */
        KeyPair keyPair = keyPairGenerator.generateKeyPair();

        /* Getting the private and public keys from the key pair, 34an ast5dmhom fl sign wl ver. */
        PrivateKey privateKey = keyPair.getPrivate();
        PublicKey publicKey = keyPair.getPublic();

        /* Creating a Signature object w bn3rf no3 el signature y3ni swa2 kant dsa aw rsa aw kda y3ni  */
        Signature signature = Signature.getInstance("SHA256withDSA");

        /* Initialize the signature */
        signature.initSign(privateKey);
        byte[] bytes = "text".getBytes();

        /* updating signature with the data and add it */
        signature.update(bytes);

        /* Calculating the signature */
        byte[] newSignature = signature.sign();

        System.out.println("Digital signature for given text in long utf: "+new String(newSignature, "UTF8")+"\n");
        System.out.println("Verification : " + ElGamalDSA.verifyDigitalSignature(text.getBytes() , newSignature, publicKey) );

    }
}
