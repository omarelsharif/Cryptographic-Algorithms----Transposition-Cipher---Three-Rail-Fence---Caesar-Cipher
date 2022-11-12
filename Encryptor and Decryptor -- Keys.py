
'''
This script prompts the user for a message,
calls on the function substitutionEncrypt to get the CipherTest message,
then calls on the substitutionDecrypt function to get the PlainText message.
The key used is: zyxwvutsrqponmlkjihgfedcba
(Key can be set to any string)
'''




def substitutionEncrypt(plainText,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText


def substitutionDecrypt(ctext,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    ctext = ctext.lower()
    plaintext = ""
    for ch in ctext:
        idx = alphabet.find(ch)
        plaintext = plaintext + key[idx]
    return plaintext

def main():
    testKey1 = "zyxwvutsrqponmlkjihgfedcba "
    message = input("Enter a message: ")
    cipherText = substitutionEncrypt(message,testKey1)
    print("CipherText: ", cipherText)
    plaintext = substitutionDecrypt("gsv jfrxp yildm ulc",testKey1)
    print("PlainText: ", plaintext)

main()
 
    
    







    
    
