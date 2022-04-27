alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while 1:
  direction = input("Type 'encode' to encrypt,type'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
  def ceaser(Direction, intext, shift_number):
    outtext = ""
    if direction == "decode":
        shift_number*=-1
    for character in intext:
      current_position = alphabet.index(character)
      
      new_position = current_position + shift_number
      new_intext = alphabet[new_position]
      outtext += new_intext
    print(f'The {direction}d word is {outtext} ')
  
  
  ceaser(Direction = direction, intext = text, shift_number= shift)
     

      
 
