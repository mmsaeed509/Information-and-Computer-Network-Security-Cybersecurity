"""
@author ozil, 0xSkorpioN
GitHub : https://github.com/mmsaeed509 , https://github.com/0xSkorpioN

"""

import hashlib # to use the Hashing Algorithm to hash the Key #
import binascii # to encode the HMAC Signature #
from base64 import encode
import HMAC

# encode the HMAC Signature, Binary data is converted to ASCII String Format #
def base64encode (signature):
    encodedSignature = binascii.b2a_base64 (signature, newline=False)
    return encodedSignature

# call HMAC class via constructor to pass the values #
def HMACGenerator(key, text=None, digestmod=''):
    return HMAC (key, text, digestmod)
    
textInput = input ("Entyer The Text : ")
keyInput = input ("Enter the Secret Key : ")

text = bytes (textInput, 'utf-8')
key = bytes (keyInput, 'utf-8')

# Generating the HMAC Signature #
# digest() returns the encoded data in byte format #
signature = base64encode (HMACGenerator (key, text, hashlib.sha256).digest ())

# Decoding the bytes object #
hmac = signature.decode("utf-8")

print("HMAC Signature : ", hmac)