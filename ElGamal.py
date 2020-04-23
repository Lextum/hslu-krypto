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


class Person:
    def __init__(self, name):
        self.name = name
        self.conversationRunning = False

    def startConversation(self):
        if self.conversationRunning:
            print('Please terminate the conversation first')
            pass
        else:
            self.conversationRunning = True
            conversationInformation = []

            self.privatePart = random.randint(1, 99999)
            self.prime = findPrime()
            self.generator = findGenerator(self.prime)

            pubKey = self.generator**self.privatePart % self.prime
            conversationInformation.append(self.prime)
            conversationInformation.append(self.generator)
            conversationInformation.append(pubKey)
            return conversationInformation

    def encryptMessage(self, message, conversationInformation):
        encryptedMessage = []

        self.privatePart = random.randint(1, 99999)
        self.prime = conversationInformation[0]
        self.generator = conversationInformation[1]

        pubKey = self.generator**self.privatePart % self.prime
        maskingKey = conversationInformation[2]**self.privatePart % self.prime

        encryptedMessage.append(pubKey)
        encryptedMessage.append(message*maskingKey % self.prime)

        print('Message ', message, '--> ', encryptedMessage[1])
        return encryptedMessage

    def decryptMessage(self, pubKey, message):
        maskingKey = pubKey**self.privatePart % self.prime

        x = 1
        while not ((x * maskingKey % self.prime) == 1):
            x = x + 1
            pass
        decryptedMessage = message * x %  self.prime
        print('Decrypt ', message, '--> ', decryptedMessage)
        return decryptedMessage
    

# a is always Alice
# b is always Bob

# Alice tells Bob he wants to send him an encrypted message

alice = Person('Alice')
bob = Person('Bob')

conversationInformation = bob.startConversation()
encryptMessage = alice.encryptMessage(123, conversationInformation)
bob.decryptMessage(encryptMessage[0], encryptMessage[1])