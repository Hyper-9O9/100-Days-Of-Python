# recreating caesar cipher using python
# the main idea is to encode and decode a message by shifting the alphabet

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt. type 'decode' to decrypte:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the number:\n"))



def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if position + shift > 25:
            new_position = (position+shift)-26

        else:
            new_position = position + shift
        new_text = alphabet[new_position]
        cipher_text += new_text

    print(f"Encrypted text is: {cipher_text}")

def decrypt(text, shift):
    decipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position-shift
        new_text = alphabet[new_position]
        decipher_text += new_text
    print(f"Decoded text is: {decipher_text}")

if direction == "encode":
    encrypt(text=text, shift=shift)
elif direction == "decode":
    decrypt(text, shift)