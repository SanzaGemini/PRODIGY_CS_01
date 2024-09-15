import string

alphabets = list(string.ascii_uppercase)
value = 0


def encrypt_upper(char):
    return alphabets[(ord(char) - 65 + value)%26]

def encrypt_lower(char):
     return alphabets[(ord(char) - 97 + value)%26].lower()

def decrypt_upper(char):
    return alphabets[(ord(char) - 65 - value)%26]

def decrypt_lower(char):
    return alphabets[(ord(char) - 97 - value)%26].lower()

def getvalue():
    while(True):
        value = input("\nPlease Enter Shift Value For Encryption: ")

        if value.isdigit():
            return int(value)
        else :
            print("Shift Value Is Not a Digit!!!")

def encrypt(text):
    results = ""
    for char in list(text):
        if char.islower():
            results += encrypt_lower(char=char)
        else: results += encrypt_upper(char=char)
    print("The word has been encrypted successfully.\n" +
          f"The word is : {results}")
    
def decrypt(text):
    results = ""
    for char in list(text):
        if char.islower():
            results += decrypt_lower(char=char)
        else: results += decrypt_upper(char=char)
    print("The word has been encrypted successfully.\n" +
          f"The word is : {results}")


def shift_cipher(text,isencrypt):
    if isencrypt:
        encrypt(text=text)
    else: decrypt(text=text)

def getmethod():
    method = input("Do you wish to encrypt or decrypt?")

    if method.lower() == "encrypt":
        return True
    elif method.lower() == "decrypt":
        return False
    elif method == "1":
        return None
    else:getmethod() 

if __name__ == "__main__":
    print("*** Welcome to Caesar Cipher Progarm ***")
    
    while(True):
        print("\n"+"If you want to end the program enter 1\n")
        
        isencrypt = getmethod()

        if isencrypt == None:
            break
        
        word = input("\nEnter a word to encrypt: ")

        value = getvalue()
        shift_cipher(word,isencrypt)

    print("\n*** Thank You For using the Caesar Cipher Progarm")    
    