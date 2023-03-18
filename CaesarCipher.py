def Encryption(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    print("Encrypted Ciphertext: "+ result)
    Decryption(result)
    


def Decryption(ciphertext):
    result = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    print("Decrypted Message: " + result)


plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift key: "))
Encryption(plaintext, shift)

