# PRODIGY_CS_01
# Caesar Cipher Program

## Overview

This Python program implements a Caesar Cipher, which is a basic encryption technique that shifts letters in the alphabet by a certain value. The program allows users to either encrypt or decrypt text based on a shift value provided by the user. Both uppercase and lowercase letters are supported.

## Features

- **Encrypt Text:** Converts the input text into encrypted form by shifting each letter by a user-defined shift value.
- **Decrypt Text:** Reverses the encryption and converts the text back to its original form by shifting in the opposite direction.
- **Handles Uppercase and Lowercase:** The program correctly processes both uppercase and lowercase letters, preserving case after encryption and decryption.
- **Interactive Input:** The user is prompted to choose between encryption and decryption, input a word, and specify the shift value.

## Functions

### `encrypt_upper(char)`
Encrypts an uppercase character by shifting it based on the user-defined value.

### `encrypt_lower(char)`
Encrypts a lowercase character by shifting it based on the user-defined value.

### `decrypt_upper(char)`
Decrypts an uppercase character by shifting it back based on the user-defined value.

### `decrypt_lower(char)`
Decrypts a lowercase character by shifting it back based on the user-defined value.

### `getvalue()`
Prompts the user to enter a shift value for the encryption. It ensures that the shift value is a valid integer.

### `encrypt(text)`
Encrypts a string of text by applying `encrypt_upper` and `encrypt_lower` to the respective characters and prints the encrypted text.

### `decrypt(text)`
Decrypts a string of text by applying `decrypt_upper` and `decrypt_lower` to the respective characters and prints the decrypted text.

### `shift_cipher(text, isencrypt)`
Determines whether to encrypt or decrypt the given text based on the `isencrypt` flag and then calls the appropriate function.

### `getmethod()`
Prompts the user to choose whether they want to encrypt or decrypt the text. Returns `True` for encryption, `False` for decryption, and `None` to end the program.

## How to Use

1. Run the program.
2. Choose whether to encrypt or decrypt.
3. Input the word to encrypt or decrypt.
4. Enter a valid shift value (a positive integer).
5. The encrypted or decrypted result will be displayed.
6. To exit the program, input `1` when prompted.

## Example

```
*** Welcome to Caesar Cipher Program ***

If you want to end the program enter 1

Do you wish to encrypt or decrypt? encrypt
Enter a word to encrypt: hello
Please Enter Shift Value For Encryption: 3
The word has been encrypted successfully.
The word is : khoor

If you want to end the program enter 1

Do you wish to encrypt or decrypt? decrypt
Enter a word to encrypt: khoor
Please Enter Shift Value For Encryption: 3
The word has been encrypted successfully.
The word is : hello
```

## Notes

- The program only encrypts and decrypts alphabetical characters. Non-alphabetical characters (like numbers, punctuation) are not handled in this code.
- Ensure that the shift value is a positive integer for the correct operation of the cipher.

## Future Improvements

- Add functionality to handle spaces and non-alphabetical characters.
- Support negative shift values for reverse operations.