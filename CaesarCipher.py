def Encryption(message, key):
    SendMessage = ''
    for i in message:
        if(ord(i)>=65 and ord(i)<=90):
            a = ord(i) + key
            if(a>90):
                a = a % 90 + 64
            SendMessage = SendMessage + chr(a)
        elif(ord(i)>=97 and ord(i)<=122):
            a = ord(i) + key
            if(a > 122):
                a = a % 122 + 96
            SendMessage = SendMessage + chr(a)
        else:
            send =  send + chr(i) + key
    print("Decrypted Message: " + SendMessage)
    Decryption(SendMessage,key)   


def Decryption(SendMessage,key):
    GetMessage = ''
    for i in SendMessage:
        if(ord(i)>=65 and ord(i)<=90):
            GetMessage = GetMessage + chr((ord(i) - key -65) % 26 + 65)
        elif(ord(i)>=97 and ord(i)<=122):
            GetMessage = GetMessage + chr((ord(i) - key - 97) % 26 + 97)
        else:
            GetMessage = GetMessage + chr(ord(i) - key)
    print("Message will get: " + GetMessage)
        

message = input("Enter the message: ")
key = int(input("Enter the key: "))

Encryption(message, key)