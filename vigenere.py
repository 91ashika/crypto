from helpers import alphabet_position, rotate_character

def encrypt(text,key):
    """ Returns text encrypted by the key """
    encrypted=""
    i=0                     # i is to iterate through the key
    for c in text:
        if c.isalpha():     #check if character is alphabet
            if i <len(key): #check if i is the length of the key to reset the value of i
                encrypted = encrypted + rotate_character(c,alphabet_position(key[i]))
                i += 1
            else:
                i = 0 
                encrypted = encrypted + rotate_character(c,alphabet_position(key[i]))   
                i += 1
        else:
            encrypted = encrypted + c

    return encrypted
            
def main():
    from sys import argv, exit
    
    if (len(argv) != 2) or (not argv[1].isalpha())  :
        print("usage: python vigenere.py keyword")
        print("Arguments:")
        print("""-keyword : The string to be used as a "key" to encrypt your message. Should only contain alphabetic characters-- no numbers or special characters.""")
        exit()

    message= input("Type a message:")
    #key= input("Encryption key:")
    key= argv[1]
    print(encrypt(message,key))
    #print(encrypt("The crow flies at midnight!","boom"))

if __name__=="__main__":
    main()    


