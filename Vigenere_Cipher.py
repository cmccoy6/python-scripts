#!/usr/bin/python3
#Author: Colin McCoy
#Date: 11/11/2021
#Version: 1.0

'''
Program is for a Vigenere Cipher

pseudocode:

1. Get the plaintext from the user
2. Get the password from the user
3. For each letter in the plaintext, rotate the letter using the password to determine the rotation.
4. Print the ciphertext
'''

plaintext = input("What would you like to encrypt? ").upper()

password = input("Choose your encryption password: ").upper()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

newletter = ""

ciphertext = ""

length = len(plaintext)

#helper function for repeating password if length > len(password)
def passPadder(password, plaintext):
    cipherKey = ""
    counter = 0
    
    while (counter < length):
        
        for letter in plaintext:
            cipherKey += password[counter % len(password)]
            counter += 1
            
    return cipherKey

#Make sure that the password matches the length of the plaintext      
if (len(password) > length):
    
    #slice the password at the appropiate length
    password = password[:length]
    
elif (len(password) < length):
    
    password = passPadder(password, plaintext)

#encryption algorithm
for index in range(0, length):
    
    #put the character in the ciphertext if it is not in the alphabet
    if plaintext[index] not in alphabet:
        ciphertext += plaintext[index]
    #otherwise perform the rotation
    else: 
        newletter = alphabet[(alphabet.find(plaintext[index]) + alphabet.find(password[index])) % 26]
        ciphertext += newletter
    
print(plaintext, ciphertext)