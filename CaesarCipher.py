#!/bin/python3
print("Wlecome to Tim's Caesar Cipher Encryption Tool!")
print('')
print('')
alphabet = 'abcdefghijklmnopqrstuvwxyz' # Defining the alphabet
key = ''
newMessage = '' #creating the storage for our encrypted message
key = input('Please input your 1-25 Caesar Cipher key: ')
print('')
print('The key you provided is: ' + key)
print('')
message = input('Please enter the message you would like to encrypt: ') # Asking for user input
    # Next we will add a 'for' loop to repeat the cipher for each character of the message
for character in message:
  if character in alphabet: # this is to exclude characters we haven't defined and therefore cannot be encrypted
    position = alphabet.find(character)             # Finding position of given character
    newPosition = position + int(key)              # Variable to define the new position by applying the Caesar Cipher
    # as it stands, if we are to enter characters such as 'y' we will get a value higher than 26, so we must address this
    newPosition = (position + int(key)) % 26 #we use the '%' here to tell the new position to go back to 0 after it reaches 26
    newCharacter = alphabet[newPosition] # here we define the new character based on the new position
    newMessage += newCharacter
  else: # this ensures that non-encypted characters are still included in the output
    newMessage += character
print('')
print('')
print('Your encrypted message is: ', newMessage)

print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('If you would like to decrypt a message please continue.')
print('')
print('')
# For the decrypting function, we use the exact same code save for one difference: we subtract the key from the input rather than adding it, thus reversing the cypher.

key = input('Please input your 1-25 Caesar Cipher key: ')
print('')
print('The key you provided is: ' + key)
print('')
newMessage = ''
message = input('Please enter the message you would like to decrypt: ')
print('')
for character in message:
  if character in alphabet: 
    position = alphabet.find(character) 
    newPosition = (position - int(key)) % 26 # applying the key in reverse
    newCharacter = alphabet[newPosition] 
    newMessage += newCharacter
  else: 
    newMessage += character
print('')
print('')
print('Your decrypted message is: ', newMessage)
print('')
print('')
print('')
print('')
input("Thanks for using Tim's Caesar Cipher Encryption tool, hit alt-f4 to end this session.")