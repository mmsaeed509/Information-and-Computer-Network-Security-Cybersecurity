package DS;

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

import java.security.*;
public class ElGamalDSA {

    public static boolean verifyDigitalSignature (byte[] input, byte[] signatureToVerify, PublicKey key) throws Exception {

        Signature signature = Signature.getInstance("SHA256withDSA");
        signature.initVerify(key);
        signature.update(input);
        return signature.verify(signatureToVerify);

    }

}
