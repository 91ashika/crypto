def alphabet_position(letter):
    """Returns alphabet's position"""
    alphabet_string="abcdefghijklmnopqrstuvwxyz"
    upper_alphabet_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in alphabet_string:
        return alphabet_string.index(letter)
    elif letter in upper_alphabet_string:
        return upper_alphabet_string.index(letter)
    else:
        return -1    

def rotate_character(char, rot):
    """Rotate a character rot times"""
    if isinstance(char,str):

        if char.isalpha() == True:
            case= char.islower()
            char_position= alphabet_position(char)
            newpos= (char_position + rot) % 26
            alphabet_string="abcdefghijklmnopqrstuvwxyz"
            if case==True:
                return alphabet_string[newpos]
            else:
                return alphabet_string[newpos].upper()    
        else:
            return char
    else:
        return char