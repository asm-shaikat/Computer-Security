import math

p = 3
q = 7

n = p*q
print("n =", n)

phi = (p-1)*(q-1)

e = 2
while(e<phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1
 
print("e =", e)

# step 5
k = 0
while(1):
    d = ((k*phi)+1)/e
    if(d == int(d)):
      break
    else:
        k += 1

print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
 
# plain text
msg = 11
print(f'Original message:{msg}')
 
# encryption
C = pow(msg, e)
C = math.fmod(C, n)
print(f'Encrypted message: {C}')
 
# decryption
M = pow(C, d)
M = math.fmod(M, n)
 
print(f'Decrypted message: {M}')