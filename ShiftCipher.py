def Encryption(message):
    SendMessage = ''
    for i in message:
        if(ord(i)>=65 and ord(i)<=90):
            a = ord(i) + 1
            if(a>90):
                a = a % 90 + 64
            SendMessage = SendMessage + chr(a)
        elif(ord(i)>=97 and ord(i)<=122):
            a = ord(i) + 1
            if(a > 122):
                a = a % 122 + 96
            SendMessage = SendMessage + chr(a)
        else:
            send =  send + chr(i) + 1
    print("Decrypted Message: " + SendMessage)
    Decryption(SendMessage)   


def Decryption(SendMessage):
    GetMessage = ''
    for i in SendMessage:
        if(ord(i)>=65 and ord(i)<=90):
            GetMessage = GetMessage + chr((ord(i) - 1 -65) % 26 + 65)
        elif(ord(i)>=97 and ord(i)<=122):
            GetMessage = GetMessage + chr((ord(i) - 1 - 97) % 26 + 97)
        else:
            GetMessage = GetMessage + chr(ord(i) - 1)
    print("Message will get: " + GetMessage)
        

message = input("Enter the message: ")

Encryption(message)