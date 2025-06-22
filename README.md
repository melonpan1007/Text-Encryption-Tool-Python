# Text-Encryption-Tool-Python

"""
This is a basic example of a substitution cipher implemented in Python.

🔐 How it Works:
- A character map `chars` is created using all printable characters (space, punctuation, digits, and letters).
- A shuffled version of this list, `key`, is used as a 1-to-1 mapping for substitution.
- During encryption:
    - Each character in the input message is found in `chars`.
    - Its index is used to find the corresponding character in `key`.
- During decryption:
    - Each character in the encrypted message is found in `key`.
    - Its index is used to retrieve the original character from `chars`.

⚠️ Note:
This cipher is not secure for real-world use. It's purely for educational or entertainment purposes.

"""
