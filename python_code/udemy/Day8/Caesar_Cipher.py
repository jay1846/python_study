alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'P', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'enocde' to encrypt, type 'decode' to decrpyt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        new_alphabet_index = alphabet.index(letter) + shift_amount
        cipher_text += alphabet[new_alphabet_index]

    print(f"Here is the encoded result: {cipher_text}")

encrypt(original_text=text, shift_amount=shift)
