import random
import math
import re

def isPrime(n):
    return not re.match(r'^.?$|^(..+?)\1+$', '1'*n)

def findPrime():
    while True:
        num = random.randint(100, 999)
        if isPrime(num):
            return num
        pass
    pass

def findGenerator(prime):
    start1 = 2
    expList = []
    genList = []
    primeElementList = list(range(1, prime-1))

    while start1 < prime:
        expList = []
        exponent = 0
        while exponent < prime:
            mod = start1**exponent % prime
            expList.append(mod)
            exponent = exponent + 1
            pass

        check = True
        for element in primeElementList:
            if element not in expList:
                check = False
                break
            pass
        if check:
            genList.append(start1)
            pass
        start1 = start1 + 1
        pass
    return genList[random.randint(0, len(genList)-1)]


# a is always Alice
# b is always Bob

p = findPrime()
g = findGenerator(p)

print('Prime:', p)
print('Generator', g)

a = random.randint(1, 99999)
b = random.randint(1, 99999)

r = (g**a) % p
s = (g**b) % p

print('Sent to Bob: ', r)
print('Sent to Alice: ', s)

keyA = s**a % p
keyB = r**b % p

print("Calculated key Alice", keyA)
print("Calculated key Bob", keyB)


