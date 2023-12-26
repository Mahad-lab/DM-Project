from math import sqrt
#required for the sqrt() function, if you want to avoid doing **0.5
import random
#required for randrange
from random import randint as rand

#just to use the well known keyword rand() from C++


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True


#initial two random numbers p,q
p = rand(1, 1000)
q = rand(1, 1000)


def generate_keypair(p, q, keysize):
    # keysize is the bit length of n so it must be in range(nMin,nMax+1).
    # << is bitwise operator
    # x << y is same as multiplying x by 2**y
    # i am doing this so that p and q values have similar bit-length.
    # this will generate an n value that's hard to factorize into p and q.

    nMin = 1 << (keysize - 1)
    nMax = (1 << keysize) - 1
    primes = [2]
    # we choose two prime numbers in range(start, stop) so that the difference of bit lengths is at most 2.
    start = 1 << (keysize // 2 - 1)
    stop = 1 << (keysize // 2 + 1)

    if start >= stop:
        return []

    for i in range(3, stop + 1, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)

    while (primes and primes[0] < start):
        del primes[0]

    #choosing p and q from the generated prime numbers.
    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_values = [q for q in primes if nMin <= p * q <= nMax]
        if q_values:
            q = random.choice(q_values)
            break
        
    n = p * q
    phi = (p - 1) * (q - 1)

    #generate public key 1<e<phi(n)
    e = random.randrange(1, phi)
    g = gcd(e, phi)

    while True:
        #as long as gcd(1,phi(n)) is not 1, keep generating e
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        #generate private key
        d = mod_inverse(e, phi)
        if g == 1 and e != d:
            break

    #public key (e,n)
    #private key (d,n)

    return (e, d, n)

def encrypt(msg_plaintext, key, n):
    string = ''

    for c in msg_plaintext:
        string = string + str(pow(ord(c), int(key), int(n))) + ' '
    
    return string


def decrypt(msg_ciphertext, key, n):

    string = ''
    cipherindex = msg_ciphertext.split(' ')
    for c in cipherindex:
        if len(c) < 1: 
            continue

        string = string + chr(pow(int(c), int(key), int(n)))

    return string


#-------------------------------------------------------------
#driver program
if __name__ == "__main__":
    bit_length = int(input("Enter bit_length: "))
    print("Running RSA...")
    print("Generating public/private keypair...")
    public, private, n = generate_keypair(
        p, q, 2**bit_length)  # 8 is the keysize (bit-length) value.
    
    print("Public Key: ", public)
    print("Private Key: ", private)

    msg = input("Write msg: ")
    encrypted_msg = encrypt(msg, public, n)

    print("Encrypted msg: ")
    print(encrypted_msg)

    print("Decrypted msg: ")
    print(decrypt(encrypted_msg, private, n))