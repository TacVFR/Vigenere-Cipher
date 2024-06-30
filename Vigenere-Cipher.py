# Vignere Cipher text is encrypted using polyaphabetic shift where in the alphabet is oredered 26 times and shifted cyclically to the left on a table in X & Y directions, the cipher will utilize different points in the table to encrypt the next point. Depends upon repeated key word 


# Encryption script will generate key untill its length is no longer the same length as the initial encryption.


def generateKey(string, key):

    key = list(key)

    if len(string) == len(key):

        return(key)

    else:

        for i in range(len(string) - len(key)):

            key.append(key[i % len(key)])

    return("" . join(key))


# Returns encrypted text using key

def cipherText(string, key):

    orig_text = []

    for i in range(len(string)):

        x = (ord(string[i]) +

            ord(key[i])) % 26

        x += ord('A')

        # i refers to looped variables

        cipher_text.append(chr(x))

    return("" . join(cipher_text))


# Decryption script

def originalText(cipher_text,  Key):

    orig_text = []

    for i in range(len(cipher_text)):

        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26

        x +=ord('A')

        orig_text.append(chr(x))

    return("" . join(orig_text))


# Driver Code

if __name__ == "__main__":

    string = "Valley Forge"

    Keyword = "SAPERE"

    key = generateKey(string, Keyword)

    cipher_text = cipherText(string,key)

    print("Ciphertext :", cipher_text)

    print("Decrypted Text :", originalText(cipher_text, key))