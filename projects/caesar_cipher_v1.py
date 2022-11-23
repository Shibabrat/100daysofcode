alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

def encrypt(text, shift):
    
        newText = []
        
        for i in range(len(text)):
            idx = alphabet.index(text[i])
            newText.append(alphabet[(idx + shift) % len(alphabet)])
        
        newText = "".join(newText)
    
        return newText

def decrypt(text, shift):
    
        newText = []
        
        for i in range(len(text)):
            idx = alphabet.index(text[i])
            newText.append(alphabet[(idx - shift) % len(alphabet)])
        
        newText = "".join(newText)
    
        return newText

if direction == "encode":
    encodedText = encrypt(text, shift)
    print(f"The encoded text is {encodedText}")

if direction == "decode":
    decodedText = decrypt(text, shift)
    print(f"The decoded text is {decodedText}")

    
