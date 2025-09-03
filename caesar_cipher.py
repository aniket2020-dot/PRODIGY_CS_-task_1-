def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shift_val = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + shift_val) % 26 + base)
        else:
            result += char
    return result

msg = input("Enter message: ")
shift = int(input("Enter shift: "))

enc = caesar_cipher(msg, shift, 'encrypt')
print("Encrypted:", enc)

dec = caesar_cipher(enc, shift, 'decrypt')
print("Decrypted:", dec)
