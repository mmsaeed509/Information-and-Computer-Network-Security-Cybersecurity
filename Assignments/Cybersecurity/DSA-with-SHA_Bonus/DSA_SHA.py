import random
from hashlib import sha256


def coprime (a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd (aa, bb):
    lastremainder, remainder = abs (aa), abs (bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod (lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


# Euclid's extended algorithm for finding the multiplicative inverse of two numbers
def modinv (a, m):
    g, x, y = extended_gcd (a, m)
    if g != 1:
        raise Exception ('Modular inverse does not exist')
    return x % m


def is_prime (num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range (3, int (num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair (p, q):
    if not (is_prime (p) and is_prime (q)):
        raise ValueError ('Both numbers must be prime.')
    elif p == q:
        raise ValueError ('p and q cannot be equal')

    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange (1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = coprime (e, phi)

    while g != 1:
        e = random.randrange (1, phi)
        g = coprime (e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = modinv (e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt (privatek, plaintext):
    # Unpack the key into it's components
    key, n = privatek

    # Convert each letter in the plaintext to numbers based on the character using a^b mod m

    numberRepr = [ord (char) for char in plaintext]
    print ("Number representation before encryption: ", numberRepr)
    cipher = [pow (ord (char), key, n) for char in plaintext]

    # Return the array of bytes
    return cipher


def decrypt (publick, ciphertext):
    # Unpack the key into its components
    key, n = publick

    # Generate the plaintext based on the ciphertext and key using a^b mod m
    numberRepr = [pow (char, key, n) for char in ciphertext]
    plain = [chr (pow (char, key, n)) for char in ciphertext]

    print ("Decrypted number representation is: ", numberRepr)

    # Return the array of bytes as a string
    return ''.join (plain)


#------------------------------------------------------------------------------------------------------

K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

def generate_hash(message: bytearray) -> bytearray:
    """Return a SHA-256 hash from the message passed.
    The argument should be a bytes, bytearray, or
    string object."""

    if isinstance(message, str):
        message = bytearray(message, 'ascii')
    elif isinstance(message, bytes):
        message = bytearray(message)
    elif not isinstance(message, bytearray):
        raise TypeError

    # Padding
    length = len(message) * 8 # len(message) is number of BYTES!!!
    message.append(0x80)
    while (len(message) * 8 + 64) % 512 != 0:
        message.append(0x00)

    message += length.to_bytes(8, 'big') # pad to 8 bytes or 64 bits

    assert (len(message) * 8) % 512 == 0, "Padding did not complete properly!"

    # Parsing
    blocks = [] # contains 512-bit chunks of message
    for i in range(0, len(message), 64): # 64 bytes is 512 bits
        blocks.append(message[i:i+64])

    # Setting Initial Hash Value
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h5 = 0x9b05688c
    h4 = 0x510e527f
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # SHA-256 Hash Computation
    for message_block in blocks:
        # Prepare message schedule
        message_schedule = []
        for t in range(0, 64):
            if t <= 15:
                # adds the t'th 32 bit word of the block,
                # starting from leftmost word
                # 4 bytes at a time
                message_schedule.append(bytes(message_block[t*4:(t*4)+4]))
            else:
                term1 = _sigma1(int.from_bytes(message_schedule[t-2], 'big'))
                term2 = int.from_bytes(message_schedule[t-7], 'big')
                term3 = _sigma0(int.from_bytes(message_schedule[t-15], 'big'))
                term4 = int.from_bytes(message_schedule[t-16], 'big')

                # append a 4-byte byte object
                schedule = ((term1 + term2 + term3 + term4) % 2**32).to_bytes(4, 'big')
                message_schedule.append(schedule)

        assert len(message_schedule) == 64

        # Initialize working variables
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7

        # Iterate for t=0 to 63
        for t in range(64):
            t1 = ((h + _capsigma1(e) + _ch(e, f, g) + K[t] +
                   int.from_bytes(message_schedule[t], 'big')) % 2**32)

            t2 = (_capsigma0(a) + _maj(a, b, c)) % 2**32

            h = g
            g = f
            f = e
            e = (d + t1) % 2**32
            d = c
            c = b
            b = a
            a = (t1 + t2) % 2**32

        # Compute intermediate hash value
        h0 = (h0 + a) % 2**32
        h1 = (h1 + b) % 2**32
        h2 = (h2 + c) % 2**32
        h3 = (h3 + d) % 2**32
        h4 = (h4 + e) % 2**32
        h5 = (h5 + f) % 2**32
        h6 = (h6 + g) % 2**32
        h7 = (h7 + h) % 2**32

    return ((h0).to_bytes(4, 'big') + (h1).to_bytes(4, 'big') + (h2).to_bytes(4, 'big') + (h3).to_bytes(4, 'big') + (h4).to_bytes(4, 'big') + (h5).to_bytes(4, 'big') + (h6).to_bytes(4, 'big') + (h7).to_bytes(4, 'big'))


def _sigma0(num: int):
    """As defined in the specification."""
    num = (_rotate_right(num, 7) ^
           _rotate_right(num, 18) ^
           (num >> 3))
    return num


def _sigma1(num: int):
    """As defined in the specification."""
    num = (_rotate_right(num, 17) ^
           _rotate_right(num, 19) ^
           (num >> 10))
    return num


def _capsigma0(num: int):
    """As defined in the specification."""
    num = (_rotate_right(num, 2) ^
           _rotate_right(num, 13) ^
           _rotate_right(num, 22))
    return num


def _capsigma1(num: int):
    """As defined in the specification."""
    num = (_rotate_right(num, 6) ^
           _rotate_right(num, 11) ^
           _rotate_right(num, 25))
    return num


def _ch(x: int, y: int, z: int):
    """As defined in the specification."""
    return (x & y) ^ (~x & z)


def _maj(x: int, y: int, z: int):
    """As defined in the specification."""
    return (x & y) ^ (x & z) ^ (y & z)


def _rotate_right(num: int, shift: int, size: int = 32):
    """Rotate an integer right."""
    return (num >> shift) | (num << size - shift)


def hashFunction (message):

    hashed = generate_hash(message.encode ("UTF-8")).hex()
    return hashed


def verify (receivedHashed, message):
    ourHashed = hashFunction (message)
    if receivedHashed == ourHashed:
        print ("Verification successful: ", )
        print (receivedHashed, " = ", ourHashed)
    else:

        print ("Verification failed")
        print (receivedHashed, " != ", ourHashed)


def main ( ):
    p = int (input ("Enter a prime number (17, 19, 23, etc): "))
    q = int (input ("Enter another prime number (Not one you entered above): "))
    # p = 17
    # q=23

    print ("Generating your public/private keypairs now . . .")
    public, private = generate_keypair (p, q)

    print ("Your public key is ", public, " and your private key is ", private)
    message = input ("Enter a message to encrypt with your private key: ")
    print ("")

    hashed = hashFunction (message)

    print ("Encrypting message with private key ", private, " . . .")
    encrypted_msg = encrypt (private, hashed)
    print ("Your encrypted hashed message is: ")
    print (''.join (map (lambda x: str (x), encrypted_msg)))
    # print(encrypted_msg)

    print ("")
    print ("Decrypting message with public key ", public, " . . .")

    decrypted_msg = decrypt (public, encrypted_msg)
    print ("Your decrypted message is:")
    print (decrypted_msg)

    print ("")
    print ("Verification process . . .")
    verify (decrypted_msg, message)


main ( )