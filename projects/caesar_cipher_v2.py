alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Combine the encrypt() and decrypt() functions into a single function called caesar(). 
# Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

def caesar(direction, text, shift):

    if direction == "decode":
        shift = -shift
    
    newText = []
        
    for i in range(len(text)):
        idx = alphabet.index(text[i])
        newText.append(alphabet[(idx + shift) % len(alphabet)])
        
    newText = "".join(newText)

    return newText

# newText = caesar(direction, text, shift)
# if direction == "encode":
#     print(f"The encoded text is {newText}")
# else:
#     print(f"The decoded text is {newText}")

newText = caesar(direction, text, shift)
print(f"The {direction}d text is {newText}")

