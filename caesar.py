from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    """Returns Encrypted text """
    newstr=""
    for c in text:
        newstr=newstr + rotate_character(c,rot)
    return newstr


def main():
    from sys import argv, exit
    
    if (len(argv) != 2) or (not argv[1].isdigit())  :
        print("usage: python caesar.py n")
        exit()
    #print(argv)
    message= input("Type a message:")
    #rotate= int(input("Rotate by:"))
    rotate = int(argv[1]) 
    #print(type(rotate))
    print(encrypt(message,rotate))
    #print(alphabet_position("Z"))
    #print(encrypt("ab, cD12",27))

if __name__=="__main__":
    main()    