from Crypto.Cipher import DES

def encrypt(key, plaintext):
    des = DES.new(key, DES.MODE_ECB)
    padded_plaintext = plaintext + (8 - len(plaintext) % 8) * chr(8 - len(plaintext) % 8)
    encrypted = des.encrypt(padded_plaintext.encode())
    return encrypted

def decrypt(key, ciphertext):
    des = DES.new(key, DES.MODE_ECB)
    decrypted = des.decrypt(ciphertext)
    return decrypted.rstrip(chr(decrypted[-1]))

key = b'secretkey'
plaintext = 'Hello, World!'
ciphertext = encrypt(key, plaintext)
print(ciphertext)
decrypted_text = decrypt(key, ciphertext)
print(decrypted_text)
