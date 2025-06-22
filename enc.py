import random
import string

# -------------------------------
# Generate character set and key
# -------------------------------

# Create a list of all possible characters (including space, punctuation, digits, and letters)
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# Create a copy and shuffle it to form a substitution key
key = chars.copy()
random.shuffle(key)

# Display the original and substituted character maps (for debugging/learning purposes)
print(f"Character Set  : {chars}")
print(f"Substitution Key: {key}")

# -------------------------------
# Encryption
# -------------------------------

# Input message to encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

# Encrypt each character by finding its index in chars and replacing it with corresponding character in key
for letter in plain_text:
    index = chars.index(letter)      # Find the index in original character set
    cipher_text += key[index]        # Substitute using the shuffled key

# Output the encrypted result
print(f"\nOriginal Message  : {plain_text}")
print(f"Encrypted Message : {cipher_text}")

# -------------------------------
# Decryption
# -------------------------------

# Input message to decrypt
cipher_text = input("\nEnter a message to decrypt: ")
plain_text = ""

# Decrypt by finding the character's index in the key and mapping back to the original chars
for letter in cipher_text:
    index = key.index(letter)        # Find the index in key
    plain_text += chars[index]       # Retrieve the original character

# Output the decrypted result
print(f"\nEncrypted Message : {cipher_text}")
print(f"Decrypted Message : {plain_text}")
