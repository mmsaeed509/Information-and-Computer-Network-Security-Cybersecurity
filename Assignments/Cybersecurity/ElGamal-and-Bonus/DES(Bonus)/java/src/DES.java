package DES;

/**
 *
 * @author ozil
 * GitHub : https://github.com/mmsaeed509
 *
 * */


// import Libs
import javax.crypto.*;
import com.sun.mail.util.BASE64DecoderStream;
import com.sun.mail.util.BASE64EncoderStream;

import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

public class DES {

    /* creating an instance of the Cipher class for encryption/decryption */
    private static Cipher encryptCipher;
    private static Cipher decryptCipher;
    private static SecretKey key;

    public DES() {

        try {

            /* Generate secret key using DES */
            key = KeyGenerator.getInstance("DES").generateKey();

            encryptCipher = Cipher.getInstance("DES");
            decryptCipher = Cipher.getInstance("DES");

            /* initialize the ciphers with the given key */
            encryptCipher.init(Cipher.ENCRYPT_MODE, key);
            decryptCipher.init(Cipher.DECRYPT_MODE, key);

        }catch (NoSuchAlgorithmException error){
            System.out.println("No Such Algorithm :" + error.getMessage());
        }catch (NoSuchPaddingException e) {
            System.out.println("No Such Padding:" + e.getMessage());
        } catch (InvalidKeyException e) {
            System.out.println("Invalid Key:" + e.getMessage());
        }

    }

    public static Cipher getEncryptCipher() {
        return encryptCipher;
    }

    public static void setEncryptCipher(Cipher encryptCipher) {
        DES.encryptCipher = encryptCipher;
    }

    public static Cipher getDecryptCipher() {
        return decryptCipher;
    }

    public static void setDecryptCipher(Cipher decryptCipher) {
        DES.decryptCipher = decryptCipher;
    }

    public static SecretKey getKey() {
        return key;
    }

    public static void setKey(SecretKey key) {
        DES.key = key;
    }

    /* initializing vector */
    private static final byte[] initialization_vector = { 22, 33, 11, 44, 55, 99, 66, 77 };

    public static String encrypt(String message) {

        try {
            /*
            * encode the string into a sequence of bytes using the named charset
            * storing the result into a new byte array.
            *
            * */
            byte[] utf8 = message.getBytes("UTF8");
            byte[] encrypt = encryptCipher.doFinal(utf8);

            /* encode to base64 */
            encrypt = BASE64EncoderStream.encode(encrypt);
            return new String(encrypt);

        } catch (Exception error) {
            error.printStackTrace();
        }
        return null;
    }

    public static String decrypt(String message) {

        try {
            /* decode with base64 to get bytes */
            byte[] decrypt = BASE64DecoderStream.decode(message.getBytes());
            byte[] utf8 = decryptCipher.doFinal(decrypt);

            /* create new string based on the specified charset */
            return new String(utf8, "UTF8");

        } catch (Exception error) {
            error.printStackTrace();
        }
        return null;
    }

}
