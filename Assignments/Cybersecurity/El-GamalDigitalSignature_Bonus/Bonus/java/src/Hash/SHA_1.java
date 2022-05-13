package Hash;

/***
 *
 * @author ozil
 * GitHub : https://github.com/mmsaeed509
 *
 * */

// import Libs
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class SHA_1 {

    public static String encryptMessage(String Message){

        try {

            /*
            *
            * SHA-1, getInstance() called together
            * this algorithm is initialized by getInstance()
            *
            * */
            MessageDigest message = MessageDigest.getInstance("SHA-1");

            /*
            *
            *  digest() is called to calculate message digest
            * returned as array of byte
            *
            * */
            byte[] messageDigest = message.digest(Message.getBytes());

            /*
            *
            * Convert byte array into Sign number
            * the '1' passed parameter refers to the Sign number
            * */
            BigInteger number = new BigInteger(1,messageDigest);

            /*
            *
            * Convert message digest into hex value
            * the '16' passed parameter refers to the hexadecimal
            * */
            String hashText = number.toString(16);

            /*
            *
            * make it 32 bit
            * by adding 0s
            *
            * */
            while (hashText.length() < 32)
                hashText = "0" + hashText;

            // returning the HashText
            return hashText;

            // to specify wrong in algorithms
        }catch (NoSuchAlgorithmException error){
            throw new RuntimeException(error);
        }

    }

}
