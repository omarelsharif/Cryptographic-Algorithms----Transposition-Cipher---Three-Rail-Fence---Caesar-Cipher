
'''This transposition cipher implements a three-rail fence that takes every third character
and puts into one of the three rails'''



def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    thirdChars = ""
    charCount = 1
    for ch in plainText:
        if charCount == 3:
            thirdChars  = thirdChars + ch
            charCount = 1
        elif charCount ==2:          
            evenChars = evenChars + ch
            charCount = 3 
      
        else:
            oddChars = oddChars + ch
            charCount = 2
        
    cipherText = thirdChars + evenChars + oddChars
    return cipherText



def main():
    plaintext = input("Enter a message: ")
    print("Plain Text: ", plaintext)
    print("CipherText: ", end = "")
    print(scramble2Encrypt(plaintext))


main()
