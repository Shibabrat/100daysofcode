# Day 8 project: Caesar cipher 
from caesar_cipher_art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = ['!','@','#','$','%','^','&','*','_','~','`',':',';','.']

continueOrNot = "yes"

def caesar(direction, text, shift):

    if direction == "decode":
        shift = -shift

    newText = []

    for i in range(len(text)):
        
        if text[i] == " " or text[i].isdigit() or text[i] in symbols:
            newText.append(text[i])
        else:
            idx = alphabet.index(text[i])
            newText.append(alphabet[(idx + shift) % len(alphabet)])

    newText = "".join(newText)

    return newText
    

while continueOrNot == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    newText = caesar(direction, text, shift)
    print(f"The {direction}d text is {newText}")

    continueOrNot = input("Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()
    
    
    
    