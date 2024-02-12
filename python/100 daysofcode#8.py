alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def main(text,shift,direction):
  l=[]
  output=""
  for i in text:
    if i in alphabet:
      l.append(alphabet.index(i))
    else:
      l.append(str(i))
  print(f"the {direction}d text is ",end=" ")
  if direction=="decode":
    shift*=-1
  for i in l:
    if type(i)==int:
      shi=i+int(shift)
    if shi > 25 or shi<-26:
      shi=shi%26
      output=output+(alphabet[shi])
    else:
      output=output+i
    

  print(output,end="")

main(text,shift,direction)
restart=input("\n\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
if restart=="yes":
  main(text,shift,direction)
else:
  print("Goodbye")

  #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 