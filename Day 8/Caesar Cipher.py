import os
import art
os.system('cls')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

go_again = True
# def encrypt(plain_text, shift_amount):
#     new_word = str()  
#     for i in plain_text:
#         position = alphabet.index(i)
#         new_position = position + shift_amount
#         if new_position > 25:
#             new_position -= 26
#         new_letter = alphabet[new_position] 
#         new_word += new_letter

#     print(f"The encoded text is {new_word}")

# def decrypt(cipher_text, shift_amount):
#     new_word = str()  
#     for i in cipher_text:
#         position = alphabet.index(i)
#         new_position = position - shift_amount
#         if new_position < 0:
#             new_position += 26
#         new_letter = alphabet[new_position] 
#         new_word += new_letter

#     print(f"The decrypted text is {new_word}")

# if direction == "encode":
#     encrypt(plain_text=text,shift_amount=shift)
# else:
#     decrypt(cipher_text=text,shift_amount=shift)

def caesar(message, shift_amount, cipher_direction):
    new_word = str()
    if cipher_direction == "decode":
        shift_amount *= -1
    for i in message:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = (position + shift_amount)%26
        # if cipher_direction == "encode":
        #     if new_position < 0:                     
        #         new_position += 26
        # elif cipher_direction == "decode":
        #     if new_position < 0:
        #         new_position += 26            
        #print(f"postition {position} new posisiton {new_position}")
        #print(f"mod new pos {new_position%26}")
            new_letter = alphabet[new_position]
        else:
            new_letter = i
        
         
        new_word += new_letter                

    print(f"The {cipher_direction}d text is {new_word}")

    
while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))    
    caesar(message=text,shift_amount=shift, cipher_direction=direction)
    go_again_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if go_again_input == "yes":
        go_again = True
    else:
        go_again = False
        print("Goodbye")