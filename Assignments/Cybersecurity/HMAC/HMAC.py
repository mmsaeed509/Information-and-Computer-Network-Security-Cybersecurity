from operator import le
import re


blocksize = 64 

# Generation of Input and Output Signatures respectively #
# Key = Padded with zeros on the left so that the result becomes 'b' bits in length #
# ipad = 00110110 (36 in Hexadecimal) repeated b/8 times #
# opad = 01011100 (5C in Hexadecimal) repeated b/8 times #
# bytes() converts an object to an immutable byte-represented object of the given size and data #

ipad = 0x36
inputSignature = bytes ((Key ^ ipad) for Key in range (256))
opad = 0x5C
outputSignature = bytes ((Key ^ opad) for Key in range (256))

# initialize class attributes using Constructor #
# key = Secret Key shared between the Sender and the Receiver #
# text = Message to be encoded #
# digestmod = Hashing Algorithm #
# 'self' to access HMAC class attributes, methods #


def __init__ (self, key, text=None, digestmod=''):

    # Returns True, if the object(digestmod) appears to be callable #
    if callable (digestmod):
        self.messageDigest = digestmod
    
    # Returns True, if digestmod is a String #
    elif isinstance (digestmod, str):
        self.messageDigest = lambda d=b'': hashlib.new(digestmod, d)

    # otherwise, Returns False #
    else:
        self.messageDigest = lambda d=b'': digestmod.new (d)

    # Assigning the variables, 'input' and 'output' #
    # to the return value of the function, 'messageDigest()' #
    self.input = self.messageDigest()
    self.output = self.messageDigest()

    # returns True if the specified object has the specified attribute #
    # otherwise False #
    if hasattr (self.input, 'block_size'):

        # block_size -> internal block size of the hash algorithm in bytes #
        blocksize = self.input.block_size
        if blocksize < 16:
            blocksize = self.blocksize

    else:
        blocksize = self.blocksize
    
    self.block_size = blocksize

    if len (key) > blocksize:
        key = self.messageDigest (key).digest()
    
    # ljust() left aligns the string using a specified character #
    # If there is a missing space in the key, it is padded with b'\0' to the right of the key #
    key = key.ljust (blocksize, b'\0')

    # translate() returns a string where some specified characters are replaced with #
    # update input/output Variables #
    self.input.update (key.translate (inputSignature))
    self.output.update (key.translate (outputSignature))

    if text is not None:
        self.update (text)
    
# @property is a decorator that makes usage of getters and setters much easier #
@property

def outputGetter(self):
    return self.output
    
def inputSetter(self, text):
    self.input.update (text)

# clone Signature, Updates the cloned value #
def current(self):
    signatureClone = self.output.copy()
    signatureClone.update (self.input.digest())
    return signatureClone

# Assigns the return value from 'current()' to signatureClone #
def digest(self):
    signatureClone = self.current()
    return signatureClone.digest()
    