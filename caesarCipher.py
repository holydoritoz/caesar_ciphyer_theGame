alphabet = [' ',',','.','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
re_run=True #flag
print(logo)
while re_run:   
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 

    def caesar(start_text,shift_amount,cipher_direction):
        end_text=''
        if cipher_direction=='decode':
            shift_amount *= -1
        for letter in start_text:
            position=alphabet.index(letter)
            new_position=position+shift_amount
            end_text += alphabet[new_position]
        print(f'The {cipher_direction} text is {end_text}')

    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

    result=input('Deseas continuar Yes or No?').lower()
    if result == 'no':
        re_run==False
        print('Goodbye')