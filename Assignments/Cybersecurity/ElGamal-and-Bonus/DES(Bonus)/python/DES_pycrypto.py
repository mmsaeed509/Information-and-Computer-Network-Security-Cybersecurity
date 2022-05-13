from Crypto.Cipher import DES
from secrets import token_bytes

def Des_Encryption(plaintext):

    cipher = DES.new (key, DES.MODE_EAX)

    nonce = cipher.nonce

    ciphertext, tag = cipher.encrypt_and_digest (plaintext.encode ('ascii'))

    return nonce, ciphertext, tag

def DES_Decryption(nonce, ciphertext, tag):

    cipher = DES.new (key, DES.MODE_EAX, nonce=nonce)

    plaintext = cipher.decrypt (ciphertext)

    try:

        cipher.verify (tag)
        return plaintext.decode ('ascii')

    except:

        return False


if __name__ == "__main__":

    key = token_bytes(8)

    print("------------------------------------------------------------")
    print("Welcome to DES Encrypt / Decrypt Program!")
    print ("-----------------------------------------------------------")

    nonce, ciphertext, tag = Des_Encryption(input ('Enter a message: '))
    plaintext = DES_Decryption(nonce, ciphertext, tag)

    print (f'Cipher text: {ciphertext}')

    if not plaintext:
        print ('Message is corrupted!')
    else:
        print (f'Plain text: {plaintext}')

