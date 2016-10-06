# ONE TIME PAD 
# Generate a random one-time-pad key and encrypt a plaintext message, outputting the ciphertext to one file and key to another.
# Python 2.7
#
# Changelog:
# Version 1.0
#	- 10/06/16: Initial Release.
#
# Possible improvements:
#	- Use os module for actual random selection (as opposed to random, which is only pseudorandom)
#	- Allow the user to select whether they want their message include spaces or not, and whether they would like to limit characters to pure alphabetical (ASCII 65-90)

# Import
import random
import os

# Specify which ascii decimal values are acceptable. Exclude spaces.
accept = range(33, 127)

# Function for converting string to ASCII while removing specified unacceptable characters
def stringToASCII(string, accept):
	listOut = []

	for char in string:
		num = ord(char)
		if num in accept:
			listOut.append(num)

	return listOut

# Function for converting ASCII back to string.
def ASCIIToString(listIn):
	stringOut = ""
	for num in listIn:
		stringOut = stringOut + chr(num)

	return stringOut

# Encrypting routine
def encrypt():

	# Have user input the plaintext message and file destinations
	print('Write your message. ASCII characters 32-126 accepted.')
	plain = raw_input("> ")

	print('Name your ciphertext output file, excluding .txt extension. For example: message1')
	print('The corresponding key will be the name with "key" appended. For example: message1key')
	fileName = raw_input("> ")


	# Convert to ASCII
	plainASCII = stringToASCII(plain, accept)


	# Make a random key of the same length as converted plaintext using all acceptable characters
	key = []

	for num in range(0,len(plainASCII)):
		key.append(random.choice(accept))


	# Use the key to create ciphertext
	cipherASCII = []

	for i in range(0,len(plainASCII)):
		encrypted = ( ( (plainASCII[i] - 33) + (key[i] - 33) ) % 94) + 33 # Note: See README for math here.
		cipherASCII.append(encrypted)


	# Convert cipher and key to strings:
	cipher = ASCIIToString(cipherASCII)
	key = ASCIIToString(key)


	# Write ciphertext to text file specified by user
	newfileName = fileName + ".txt"
	file = open(newfileName,"w")
	file.write(cipher)
	file.close()


	# Write key to filename
	keyFile = fileName + "key.txt"
	file = open(keyFile,"w")
	file.write(key)
	file.close()

# Decrypting routine
def decrypt():

	# Ask user to input file names
	print('Enter the name of the ciphertext file, excluding the extension.\n (For example: message1 for message1.txt)')
	cipherFile = raw_input('> ')

	print('Enter the name of the key file, excluding the extension.\n (For example: message1key for message1key.txt')
	keyFile = raw_input('> ')


	# Open files and extract strings
	file = open(cipherFile + ".txt","r")
	cipher = file.read()
	file.close()

	file = open(keyFile + ".txt","r")
	key = file.read()
	file.close()

	# Convert the strings to ASCII
	cipherASCII = stringToASCII(cipher, accept)
	keyASCII = stringToASCII(key, accept)

	# Decrypt the ciphertext
	plainASCII = []

	for i in range(0,len(cipherASCII)):
		decrypted = ( ( (cipherASCII[i] - 33) - (keyASCII[i] - 33) ) % 94) + 33 # Note: See README for math here.
		plainASCII.append(decrypted)


	# Convert plaintext ASCII to string
	plain = ASCIIToString(plainASCII)

	# Write plaintext to text file specified by user
	plainFileName = cipherFile + "plain.txt"
	file = open(plainFileName,"w")
	file.write(plain)
	file.close()





# MAIN LOOP

while True:
	# Ask the user which function to use
	print('Choose a mode:\n (1) Encrypt a message\n (2) Decrypt files\n (3) Quit')
	mode = int(raw_input('> '))

	# Run the selected function
	if mode == 1:
		encrypt()
		print('Encryption successful.\n\n')
	elif mode == 2:
		decrypt()
		print('Decryption successful. Remember that the spaces are gone!\n\n')
	else:
		print('Goodbye.')
		break