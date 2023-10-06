#!/usr/bin/python3
#Author: Colin McCoy
#Date: 11/11/2021
#Version: 1.0

'''
Program for decrypting the ciphertext back to plaintext. 

pseudocode:

1. Get the ciphertext from the user
2. Get the password from the user
3. For each letter in the plaintext, rotate the letter using the password to determine the rotation.
4. Print the plaintext
'''

ciphertext = input("What would you like to decrypt? ").upper()

password = input("Choose your encryption password: ").upper()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

newletter = ""

plaintext = ""

length = len(ciphertext)

#helper function for repeating password if length > len(password)
def passPadder(password, ciphertext):
    cipherKey = ""
    counter = 0
    
    while (counter < length):
        
        for letter in ciphertext:
            cipherKey += password[counter % len(password)]
            counter += 1
            
    return cipherKey

#Make sure that the password matches the length of the ciphertext      
if (len(password) > length):
    
    #slice the password at the appropiate length
    password = password[:length]
    
elif (len(password) < length):
    
    password = passPadder(password, ciphertext)

#decryption algorithm
for index in range(0, length):
    
    #put the character in the ciphertext if it is not in the alphabet
    if ciphertext[index] not in alphabet:
        plaintext += ciphertext[index]
    #otherwise perform the rotation
    else:
        #just subtract to undo, even if the result is negative, it will count from the back of the string, which isn't zero indexed going backwards. 
        newletter = alphabet[(alphabet.find(ciphertext[index]) - alphabet.find(password[index]))]
        plaintext += newletter
    
print(ciphertext, plaintext)