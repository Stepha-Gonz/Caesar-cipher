
from logo import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_program= False


def caesar(input_text, shift_amount,code_decode):
    output_text=""
    if code_decode == "decode":
        shift_amount *= -1
    for letter in input_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the final result: {output_text}")


while not end_program:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    option=input("end program? Y or N: \n").upper()
    if option == "Y":
        end_program=True


