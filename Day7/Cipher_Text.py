import logo
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(logo.logo)
direction = input("Type `encode` to encrypt, type `decode` to decrypt\n").lower()
text = input("enter the text\n").lower()
shift = int(input("Enter the number to shift\n"))


def caesar(original_text,shift_amount,encode_or_decode):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if encode_or_decode == 'encode':
                new_index = (index + shift_amount) % len(alphabet)
                cipher_text += alphabet[new_index]
            elif encode_or_decode == 'decode':
                new_index = (index - shift_amount) % len(alphabet)
                cipher_text += alphabet[new_index]
    
    if encode_or_decode == 'encode':
        print(f"here is the encoded result: {cipher_text}")
    elif encode_or_decode == 'decode':
        print(f"here is the decoded result: {cipher_text}")
                  
caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

