import random

def generate_primes():
    primes = []
    while len(primes) < 2:
        p = random.randint(1, 100)
        if is_prime(p):
            primes.append(p)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    g, x, y = gcd_extended(a, m)
    if g != 1:
        return None
    return x % m

def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd_extended(b % a, a)
        return (g, x - (b // a) * y, y)

def encrypt(message, n, e):
    return pow(message, e, n)

def decrypt(ciphertext, n, d):
    return pow(ciphertext, d, n)

def generate_key_pair():
    primes = generate_primes()
    p = primes[0]
    q = primes[1]
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = mod_inverse(e, phi)
    return (n, e), (n, d)

def main():
    message = int(input("Enter message: "))
    public_key, private_key = generate_key_pair()
    print("Public key: ", public_key)
    print("Private key: ", private_key)
    encrypted_message = encrypt(message, public_key[0], public_key[1])
    decrypted_message = decrypt(encrypted_message, private_key[0], private_key[1])
    print("Original message: ", message)
    print("Encrypted message: ", encrypted_message)
    print("Decrypted message: ", decrypted_message)

if __name__ == "__main__":
    main()
