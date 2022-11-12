''' This cipher is named after Julius Caesar, who used this cryptographic system.
It encrypts a message by rotating the plaintext character by 13 positions in the alphabet.
Ie: “a” becomes “n”; likewise, “n” becomes “a.” '''



def rot13(word, crypt):
    x = len(word)
    word = word.lower()
    wword = []
    wword[:] = word
    newlist = []
    for i in range(0,x):
        newlist.append(" ")

    for i in range (0,x):
        newlist[i] = ord(wword[i])

    for i in range(0,x):
        newlist[i] += 13
        
    for i in range(0,x):
        if newlist[i] > 122:
            newlist[i] -= 26
            
    for i in range (0,x):
        newlist[i] = (chr(newlist[i]))
        
    if crypt == "encrypt":
        print ("After encrypting ", word," the cipherText message is ", end ="")
        
    if crypt == "decrypt":
        print ("After decrypting ", word," the plainText message is ", end ="")

    for i in range(0,x):
        
        print ((newlist[i]), end = "")
    cypher = ""
    
    for i in range(0,x):
        cypher += newlist[i]

    #print(cypher)
    return cypher


def main():
    
    word = input("Enter text message: ")
    z = rot13(word, "encrypt")
    print (" ")
    rot13(z,"decrypt")    

    
main()
