"""
        RSA Algorithm Implementation In python
        @author: Mahmoud
        @GitHub : mmsaeed509

Team :-

        Name :-                                ID :-

                Mahmoud Mohamed Said Ahmed           20180261

                Omar Ismael Mohamed                  20180173

                Hasan Khames                         20180087

"""
import random


# Check If Number IS Prime Or Not
# Fermat’s Primality Test Function To Check The Primality Of The Numbers Chosen In The Running
def fermatTest(number):
    return pow(2, number - 1, number) == 1


# isPrime Function To Define Number Prime Or Not
def isPrime(number):
    if not fermatTest(number):
        return False
    else:
        return True


# Calculation Of GCD -> e Must Be CoPrime And [ 1 < e < ϕ]
def GDC(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def eGCD(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = eGCD(b % a, a)
        return g, x - (b // a) * y, y


def generateKey():
    print("************************************************")
    print("*    RSA Algorithm Implementation In python    *")
    print("************************************************")
    print()

    # Input Prime Numbers
    print("Please Enter The 'p' And 'q' Values Below:")
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    print("************************************************")

    check_p_isPrime = isPrime(p)
    check_q_isPrime = isPrime(q)

    while (check_p_isPrime == False) or (check_q_isPrime == False):
        p = int(input("Enter a prime number for p: "))
        q = int(input("Enter a prime number for q: "))
        check_p_isPrime = isPrime(p)
        check_q_isPrime = isPrime(q)

    print()
    print("************************************************")
    print("p value = ", p, "    q value = ", q)
    print("************************************************")
    print()

    # Calculation Of RSA Modulus -> n
    n = p * q
    print("RSA Modulus -> n = ", n)
    print()

    # Calculation Of Euler's Toitent -> r ϕ
    r = (p - 1) * (q - 1)
    print("Euler's Toitent -> r = ", r)
    print()

    # Find CoPrime Value Between 1 < e < ϕ
    e = random.randint(1, r)
    g = GDC(e, r)
    while g != 1:
        e = random.randint(1, r)
        g = GDC(e, r)

    print("************************************************")
    print("CoPrime e : ", e)
    print("************************************************")
    print()

    # Modular Inverse d
    d = eGCD(e, r)[1]
    d = d % r
    if d < 0:
        d += r
    return (e, n), (d, n)


publicKey, privateKey = generateKey()
print("Public Key : ", publicKey)
print("Private Key : ", privateKey)


# Encryption
def encrypt(text, public_Key):
    key, n = public_Key
    cipherText = [pow(ord(char), key, n) for char in text]
    return cipherText


# Decryption
def decrypt(cipherText, private_Key):
    try:
        key, n = private_Key
        text = [chr(pow(char, key, n)) for char in cipherText]
        return "".join(text)
    except TypeError as e:
        print(e)


# Text That You Want To Encrypt/Decrypt
print("************************************************")
message = input("What Would You Like To Encrypt : ")
print("Your message is:", message)
print("************************************************")
print()

encryptedMessage = encrypt(message, publicKey)
print("************************************************")
print("Encrypted Message : ", encryptedMessage)
print("************************************************")
print()
decryptedMessage = decrypt(encryptedMessage, privateKey)
print("************************************************")
print("Decrypted Message : ", decryptedMessage)
print("************************************************")
print()
