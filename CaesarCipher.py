import string

alphabets = list(string.ascii_uppercase)
shiftValue = 0

def encryptUpper(char):
    """
    Encrypts an uppercase letter using Caesar cipher.

    Args:
    char (str): A single uppercase character to be encrypted.

    Returns:
    str: Encrypted uppercase letter.
    """
    return alphabets[(ord(char) - 65 + shiftValue) % 26]

def encryptLower(char):
    """
    Encrypts a lowercase letter using Caesar cipher.

    Args:
    char (str): A single lowercase character to be encrypted.

    Returns:
    str: Encrypted lowercase letter.
    """
    return alphabets[(ord(char) - 97 + shiftValue) % 26].lower()

def decryptUpper(char):
    """
    Decrypts an uppercase letter using Caesar cipher.

    Args:
    char (str): A single uppercase character to be decrypted.

    Returns:
    str: Decrypted uppercase letter.
    """
    return alphabets[(ord(char) - 65 - shiftValue) % 26]

def decryptLower(char):
    """
    Decrypts a lowercase letter using Caesar cipher.

    Args:
    char (str): A single lowercase character to be decrypted.

    Returns:
    str: Decrypted lowercase letter.
    """
    return alphabets[(ord(char) - 97 - shiftValue) % 26].lower()

def getShiftValue():
    """
    Prompts the user to enter a valid shift value for encryption.

    Returns:
    int: The shift value entered by the user.
    """
    while(True):
        value = input("\nPlease Enter Shift Value For Encryption: ")

        if value.isdigit():
            return int(value)
        else:
            print("Shift Value Is Not a Digit!!!")

def getResults(results):
    return f"The Word is: {results}"

def encrypt(text):
    """
    Encrypts a given text using Caesar cipher.

    Args:
    text (str): The text to be encrypted.

    Returns:
    None
    """
    results = ""
    for char in list(text):
        if char.islower():
            results += encryptLower(char=char)
        elif char.isupper():
            results += encryptUpper(char=char)
        else:
            results += char
    print("The Word Has Been Encrypted Successfully.\n" +
          getResults(results))
    
def decrypt(text):
    """
    Decrypts a given text using Caesar cipher.

    Args:
    text (str): The text to be decrypted.

    Returns:
    None
    """
    results = ""
    for char in list(text):
        if char.islower():
            results += decryptLower(char=char)
        elif char.isupper():
            results += decryptUpper(char=char)
        else:
            results += char
    print("The Word Has Been Decrypted Successfully.\n" +
          getResults(results=results))

def shiftCipher(isEncrypt):
    """
    Encrypts or decrypts the given text based on user input.

    Args:
    isEncrypt (bool): If True, the function encrypts; if False, it decrypts.

    Returns:
    None
    """
    text = getWord(isEncrypt)
    if isEncrypt:
        encrypt(text=text)
    else:
        decrypt(text=text)

def getMethod():
    """
    Prompts the user to choose between encryption and decryption.

    Returns:
    bool: True if the user chooses encryption, False if decryption.
    None: If the user wants to exit the program.
    """
    method = input("Do You Wish To Encrypt Or Decrypt? ")

    if method.lower() == "encrypt":
        return True
    elif method.lower() == "decrypt":
        return False
    elif method == "1":
        return None
    else:
        return getMethod()

def getWord(isEncrypt):
    """
    Prompts the user to enter the text to be encrypted or decrypted.

    Args:
    isEncrypt (bool): Determines whether the text will be encrypted or decrypted.

    Returns:
    str: The text entered by the user.
    """
    if isEncrypt:
        return input("\nEnter A Word To Encrypt: ")
    return input("\nEnter A Word To Decrypt: ")

if __name__ == "__main__":
    print("*** Welcome To Caesar Cipher Program ***")
    
    while(True):
        print("\nIf You Want To End The Program Enter 1\n")
        
        isEncrypt = getMethod()

        if isEncrypt == None:
            break

        shiftValue = getShiftValue()
        shiftCipher(isEncrypt)

    print("\n*** Thank You For Using the Caesar Cipher Program ***")
