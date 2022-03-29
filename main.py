from art import logo, MORSE_CODE_DICT
from os import system, name


# define our clear function

def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')
    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


def decrypt(morse_word):
    decoded_word = ""
    morse_letters = morse_word.strip().split(" ")
    for alpha in morse_letters:
        for key, value in MORSE_CODE_DICT.items():
            if value == alpha:
                decoded_word += key
    return decoded_word


def program(pro):
    if pro == "y":

        # Takes Input to be encoded from user
        input_text = input("Write the text you want to encode in Morse Code\n").upper()

        # Encoding
        code = ""
        for letter in input_text:
            try:
                if letter == ' ':
                    code += "/"
                else:
                    code += f"{MORSE_CODE_DICT[letter]} "
            except KeyError:
                print(f"Unfortunately The letter '{letter}' couldn't be encoded into morse code")

        print(f"Your text: {input_text}")
        print(f"Morse code : {code}")

    elif pro == "n":

        # Decoding
        decode_input = input("Please enter the Morse code below:\n")
        if decode_input.split(" ")[0] not in MORSE_CODE_DICT.values():
            print("This is an invalid Morse code, Please try again.")
            return
        else:
            decrypted_code = ""
        for code_word in decode_input.split("/"):
            word = decrypt(code_word)
            decrypted_code += f"{word} "
        print(f"Your code: {decode_input}")
        print(f"Decoded text: {decrypted_code}")

    else:
        print("You Pressed the wrong Button, Please try again")


is_on = True
while is_on:
    print(logo)
    input_pro = input("Press 'Y' to Encode and 'N' to Decode\n").lower()
    program(input_pro)
    press_key = input("Press any key to run again. or 'e' to exit program").lower()
    if press_key == "e":
        is_on = False
    else:
        clear()
