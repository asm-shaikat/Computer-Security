def Encryption(x,k):
    send = ''
    for i in x:
        if ( ord(i) >= 65 and ord(i) <= 90 ):
            a = ord(i) + k
            if(a>90):
                a = a % 90 + 64
            send = send + chr(a)
        elif( ord(i) >= 97 and ord(i) <= 122 ):
            a = ord(i) + k
            if(a>122):
                a = a % 122 + 96
            send = send + chr(a)
        else:
            send  = send + ord(i) + k
    print("Message which is send: " + send)
    Decription(send)

def Decription(send):
    get = ''
    for j in send:
        if( ord(j) >= 65 and ord(j) <= 90 ):
            get = get + chr((ord(j) - k - 65)%26+65)
        elif( ord(j) >= 97 and ord(j) <= 122 ):
            get = get + chr((ord(j) - k - 97)%26+ 97)
        else:
            get = get + chr((ord(j) - k))
    print("Message which is received: " + get)


x = input("Enter message to be encrypted: ")

k = int(input("Enter key: "))

Encryption(x,k)