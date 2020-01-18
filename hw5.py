'''
HOMEWORK 5 FULL

Name: Clara
Andrew ID: zixuany
'''

import random

'''
PART 1: Caesar Cipher

Encryption: A caesar cipher shifts the characters in a string by a set amount.
For example, a shift of 5 would mean all a's would become f's, b's become g's,
and z's would become an e's, because we shift the value back around. All characters
that are not letters should not be shifted for this assignment.

Decryption: To decrypt a Caesar Cipher, you would need to know the shift and
reverse it. However, this shift could be easily stolen. One can
repeatedly shift the encoded string over and over and look for common words
that appear. For example, the word "the" is a short word and very common.
If we find many instances of common words, we probably have the right shift.
'''

'''
caesar_encrypt(string,shift) takes a string of characters and a shift 0-25,
makes the string lowercase and returns a new string with the letters shifted and 
all other characters left alone.

Note 1: you should be using ord(letter) to get the ASCII value of a letter and 
chr(int) to get the letter associated with an ASCII integer.

For example: caesar_encrypt("The dog jumps over the fox.",4)
returns "xli hsk nyqtw sziv xli jsb."
'''
def caesar_encrypt(string,shift):
    newstring = ""
    string = string.lower()
    for char in string:
        if char.isalpha():
            if ord(char) + shift > ord("z"):
                newstring += chr(ord(char) + shift - 26)
            else:
                newstring += chr(ord(char) + shift)
        else:
            newstring += char
    return newstring

'''
caesar_decrypt(string) takes a string of letters and spaces, and
repeatedly shifts the message until "the " appears in the string, which means it is 
decrypted. Then return this decrypted message.

Note 1: you should look for "the " including the space because it is
possible for other words to include "the" in them when encrypted. For example,
caesar_encrypt("drop",18) = "thef" which includes "the" as a substring but is
not as popular a word.

Note 2: you may find it helpful to use caesar_encrypt() in your decrypt function.

For example: caesar_decrypt("xli hsk nyqtw sziv xli jsb.")
returns "the dog jumps over the fox."
'''
def caesar_decrypt(string):
    string = string.lower()
    shift = 1
    while string.find("the ") == -1:
        string = caesar_encrypt(string, shift)
    return string

'''
PART 2: Substitution Cipher

Generate Substitution List: If two people agree that they have encrypted
messages to send each other, they can create a random shuffle (permutation) of all
the letters in the alphabet and share it between them. This is the secret list
that they will use to encypt and decrypt their messages.

Encryption: When they have a message to send, for each letter of their message, 
if the letter is the i'th letter of the alphabet, they'll substitute in the i'th 
letter of their secret list.

Decryption: When receiving an encrypted message, they look in the secret list for 
the index of each letter of their message, and substitute it for the letter at 
that index in the normal alphabet.

'''

'''
generate_cipher_alphabet() should return a list of letters that represents a 
random shuffle of the alphabet.

You should use the function random.sample(alphabet,length) which takes a string
containing each and every lower case letter in the English alphabet and the
length of that string, and returns a list of the letters in a random order.
'''
def generate_cipher_alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    length = 26
    ciphabet = random.sample(alphabet,length)
    return ciphabet

'''
substitution_encrypt(message,secret) should return the cipher (encrypted string)
of the message string encoded using the secret list. In particular, first make
the message lower case and then for each letter of the message (if the letter is
the i'th letter of the alphabet), substitute it for the i'th letter of their
secret list. Any characters that are not letters should be kept the same.

For example:
substitution_encrypt("The dog jumps over the fox.",["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d"])
returns "xli hsk nyqtw sziv xli jsb."
'''
def substitution_encrypt(message,secret):
    message = message.lower()
    newstring = ""
    for char in message:
        if char.isalpha():
            newstring += secret[ord(char)-ord("a")]
        else:
            newstring += char
    return newstring

'''
substitution_decrypt(cipher,secret) should return the original message
of the decrypted cipher string using the secret list. In particular, for each
letter of the ciper (if the letter is the i'th letter of the secret list),
substitute it for the i'th letter of the original alphabet. Any characters that
are not letters should be kept the same.

For example:
substitution_decrypt("xli hsk nyqtw sziv xli jsb.",["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d"])
returns "The dog jumps over the fox."
'''
def substitution_decrypt(cipher,secret):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newstring = ""
    for char in cipher:
        if char.isalpha():
            i = secret.index(char)
            newstring += alphabet[i]
        else:
            newstring += char
    return newstring


##################################################

def test_caesar_encrypt():
    print("testing caesar_encrypt...",end="")
    assert(caesar_encrypt("The dog jumps over the fox",4) == "xli hsk nyqtw sziv xli jsb")
    assert(caesar_encrypt("the Dog Jumps over thE fox",4) == "xli hsk nyqtw sziv xli jsb")
    assert(caesar_encrypt("drop the bucket",16) == "thef jxu rksauj")
    assert(caesar_encrypt("DrOp the Bucket",16) == "thef jxu rksauj")
    assert(caesar_encrypt("Encryption is the coolest",10) == "oxmbizdsyx sc dro myyvocd")
    print("...done!",)

def test_caesar_decrypt():
    print("testing caesar_decrypt...",end="")
    assert(caesar_decrypt("xli hsk nyqtw sziv xli jsb") == "the dog jumps over the fox")
    assert(caesar_decrypt("thef jxu rksauj") == "drop the bucket")
    assert(caesar_decrypt("oxmbizdsyx sc dro myyvocd") == "encryption is the coolest")
    print("...done!")

def test_caesar_cipher():
    print("testing caesar cipher (all)...",end="")
    s = "the dog is brown"
    assert(s.lower() == caesar_decrypt(caesar_encrypt(s,6)))
    s = "This Is the best SENTence"
    assert(s.lower() == caesar_decrypt(caesar_encrypt(s,1)))
    s = "I Think the class Is Great!"
    assert(s.lower() == caesar_decrypt(caesar_encrypt(s,19)))
    print("...done!")

def test_generate_cipher_alphabet():
    print("testing generate_cipher_alphabet",end="")
    for i in range(10):
        order = generate_cipher_alphabet()
        assert(len(order) == 26)
        for o in order:
            assert(o in "abcdefghijklmnopqrstuvwxyz")
    print("...done")

def test_substitution_encrypt():
    print("testing substitution_encrypt...",end="")
    c = ["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d"]
    assert(substitution_encrypt("The dog jumps over the fox",c) == "xli hsk nyqtw sziv xli jsb")
    assert(substitution_encrypt("the Dog Jumps over thE fox",c) == "xli hsk nyqtw sziv xli jsb")
    c = ["q","r","s","t","u","v","w","x","y","z","a","b","c","d", "e","f","g","h","i","j","k","l","m","n","o","p",]
    assert(substitution_encrypt("drop the bucket",c) == "thef jxu rksauj")
    assert(substitution_encrypt("DrOp the Bucket",c) == "thef jxu rksauj")
    c = ["k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d", "e","f","g","h","i","j"]
    assert(substitution_encrypt("Encryption is the coolest",c) == "oxmbizdsyx sc dro myyvocd")
    print("...done!",)

def test_substitution_decrypt():
    print("testing substitution_decrypt...",end="")
    c = ["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d"]
    assert(substitution_decrypt("xli hsk nyqtw sziv xli jsb",c) == "the dog jumps over the fox")
    c = ["q","r","s","t","u","v","w","x","y","z","a","b","c","d", "e","f","g","h","i","j","k","l","m","n","o","p",]
    assert(substitution_decrypt("thef jxu rksauj",c) == "drop the bucket")
    c = ["k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d", "e","f","g","h","i","j"]
    assert(substitution_decrypt("oxmbizdsyx sc dro myyvocd",c) == "encryption is the coolest")
    print("...done!")

def test_substitution_cipher():
    print("testing substitution cipher (all)...",end="")
    c = generate_cipher_alphabet()
    s = "this is a dog"
    assert(s.lower() == substitution_decrypt(substitution_encrypt(s,c),c))
    c = generate_cipher_alphabet()
    s = "This Is a SENTence"
    assert(s.lower() == substitution_decrypt(substitution_encrypt(s,c),c))
    c = generate_cipher_alphabet()
    s = "I Think This Is Great!"
    assert(s.lower() == substitution_decrypt(substitution_encrypt(s,c),c))
    print("...done!")

def testAll():
    test_caesar_encrypt()
    test_caesar_decrypt()
    test_caesar_cipher()
    test_generate_cipher_alphabet()
    test_substitution_encrypt()
    test_substitution_decrypt()
    test_substitution_cipher()

testAll()