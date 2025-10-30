"""
RSA.py

Lab: Secure Communication with RSA, DES, and Raspberry Pi GPIO

Your task:
-----------
Implement the RSA functions below:
- gcd
- multiplicative_inverse
- is_prime
- generate_keypair
- encrypt
- decrypt

You will use these functions in both chat and image client/server code.

Notes:
- Work step by step. First get gcd() working, then move to modular inverse, etc.
- Test your implementation with the provided example at the bottom.
"""

import random

def gcd(a, b):
    """
    Compute the greatest common divisor of a and b.
    """
    # TODO: implement Euclidean algorithm
    stop = 0
    gcd = 0

    while (stop == 0):
        c = a % b

        if c == 0:
            gcd = b
            stop = 1
        else:
            a = b
            b = c
    
    return gcd
        

def multiplicative_inverse(e, phi):
    """
    Compute the modular inverse of e modulo phi.
    Returns d such that (d*e) % phi == 1
    """
    # TODO: implement Extended Euclidean Algorithm
    x0, x1 = 0, 1
    r0, r1 = phi, e

    while (r1 != 0):
        q = r0 // r1
        r0, r1 = r1, r0 - q*r1
        x0, x1 = x1, x0 - q*x1

    return x0 % phi


def is_prime(num):
    """
    Check if a number is prime.
    Return True if prime, False otherwise.
    """
    # TODO: implement primality check
    if num < 2:
        return False
    else:
        for i in range(2, num/2 + 1):
            if num % i == 0:
                return False
        
        return True


def generate_keypair(p, q):
    """
    Generate RSA keypair given two primes p and q.
    Returns (public, private) where:
    - public = (e, n)
    - private = (d, n)
    """
    # TODO: implement RSA keypair generation
    # Steps:
    # 1. Compute n = p * q
    # 2. Compute phi = (p-1)*(q-1)
    # 3. Choose e such that gcd(e, phi) = 1
    # 4. Compute d = multiplicative_inverse(e, phi)
    n = p*q
    phi = (p-1)*(q-1)
    e_list = []

    for i in range(1, n):
        if gcd(i, phi) == 1:
            e_list.append(i)
    
    e = random.choice(e_list)
    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    """
    Encrypt plaintext using key pk = (e or d, n).
    Plaintext is a string; return a list of integers (ciphertext).
    """
    # TODO: implement RSA encryption
    ciphertext = []
    e, n = pk

    for i in plaintext:
        i = ord(i)
        i = (i**e) % n
        ciphertext.append(i)
    
    return ciphertext


def decrypt(pk, ciphertext):
    """
    Decrypt ciphertext using key pk = (e or d, n).
    Ciphertext is a list of integers; return a string (plaintext).
    """
    # TODO: implement RSA decryption
    plaintext_list = []
    d, n = pk

    for i in ciphertext:
        i = (i**d) % n
        plaintext_list.append(chr(i))
    
    plaintext = "".join(plaintext_list)

    return plaintext


# --- Example test case ---
if __name__ == "__main__":
    print("RSA Test Example")

    # Example primes (small for testing)
    p, q = 61, 53
    public, private = generate_keypair(p, q)

    print("Public key:", public)
    print("Private key:", private)

    message = "HELLO"
    print("Original message:", message)

    encrypted_msg = encrypt(public, message)
    print("Encrypted message:", encrypted_msg)

    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted message:", decrypted_msg)