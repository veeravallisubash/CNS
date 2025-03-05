def caesar_cipher(text, shift):
    result = ""
    
    # Loop through each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If the character is not a letter, just add it unchanged
            result += char
            
    return result

# Test the Caesar Cipher
if __name__ == "__main__":
    text = "Hello, World!"  # Example input
    shift = 3  # Shift value
    encrypted = caesar_cipher(text, shift)  # Encrypting the text
    print(f"Encrypted Text: {encrypted}")

    # Decrypting back (using the negative shift)
    decrypted = caesar_cipher(encrypted, -shift)
    print(f"Decrypted Text: {decrypted}")
def caesar_cipher(text, shift):
    result = ""
    
    # Loop through each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If the character is not a letter, just add it unchanged
            result += char
            
    return result

# Test the Caesar Cipher
if __name__ == "__main__":
    text = "Hello, World!"  # Example input
    shift = 3 
    encrypted = caesar_cipher(text, shift)
    print(f"Encrypted Text: {encrypted}")

    decrypted = caesar_cipher(encrypted, -shift)
    print(f"Decrypted Text: {decrypted}")
