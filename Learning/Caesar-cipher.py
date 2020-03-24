#Caesar cipher - Implement a Caesar cipher, both encoding and decoding.
#The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z).
#The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A).
#So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC".
#This simple "monoalphabetic substitution cipher" provides almost no security,
#because an attacker who has the encoded message can either use frequency analysis to guess the key,
#or just try all 25 keys

#dictionary containing letters and corresponding values
cipher = {' ':0,'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
decipher = {0:' ',1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
alpha = ['a','b','c','d','e','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#function to convert a string into a sequence of letters.
def string_convert(string):
    conversion = []
    for let in list(string.lower()):
        conversion.append(cipher[let])
    return conversion

# function to "encode" the message
def encode(conversion, key):
    encoded = []
    for i in conversion:
        if i+key <= 26 and i != 0:
            encoded.append(i+key)
        elif i+key > 26:
            eoded.append((i+key)-26)
        elif i == 0:
            encoded.append(i)
    return encoded

# a combined function which takes a string, converts it into a list of integers
# and then encodes it, before eventually reconverting it into a string.

def encoder(string,key):
    conversion = []
    for let in list(string.lower()):
        conversion.append(cipher[let])

    encoded = []
    for i in conversion:
        if i+key <= 26 and i != 0:
            encoded.append(i+key)
        elif i+key > 26:
            encoded.append((i+key)-26)
        elif i == 0:
            encoded.append(i)
    return encoded

# a function which "decodes": takes a series of numbers and number-key
#converts the series of numbers into a string of letters.
def decoder(numbers, key):
    decode = []
    for i in numbers:
        if i == 0:
            decode.append(i)
        elif i-key >0:
            decode.append(i-key)
        elif i-key <=0:
            decode.append((i-key)+26)

    to_text = []
    for i in decode:
        to_text.append(decipher[i])
    return ''.join(to_text)

# function to ask for a string input
def string_input():
    while True:
        string_test = input("Type in the text that you would like to encrypt:\n ")
        if any(char.isdigit() for char in string_test) == False:
            print("Text accepted.")
            return string_test
        else:
            print("Error: Your text may not contain any digits.")
            continue
# function which asks for an encryption key
def ask_for_key():
    while True:
        try:
            key_check = int(input("Please enter the key (number 0 to 26):\n"))
        except ValueError:
            print("Sorry, you may only enter digits.")
        else:
            if key_check <0 or key_check > 26:
                print("Sorry, your key may not be less than 0 or greater than 26")
            else:
                print("Your key has been entered.\n")
                return key_check

# a function that decrypts a number sequence
def number_input():
    decode_list = []
    while True:
        print("Enter the number sequence that you would like to decrypt.")
        number_test = input("Enter each number seperated by a space:\n ")

        if number_test.isupper() or number_test.islower() == True:
            print("Sorry, you may only enter digits.\n")
        else:
            for i in number_test.split():
                if int(i) < 0 or int(i)>26:
                    print("A digit less than 0 or greater than 26 has been excluded.")
                    continue
                else:
                    decode_list.append(int(i))
            print("Sequence accepted as:\n")
            print(decode_list)
            return decode_list

# Below is the running of the cipher program
print("This is a Caesar cipher encoder and decoder.")
print("It can encrypt or decrypt a text with a key.")

coding = True

while coding:

    choosing = True
    while choosing == True:
        choice = input("Do you want to encrypt or decrypt ? 'e' or 'd': \n")

        if choice.lower() == 'e':
            print("\nYou have choosen to encrypt a text.\n")
            encode = True
            choosing = False
        elif choice.lower() == 'd':
            print("\nYou have choosen to decrypt a text.\n")
            encode = False
            choosing = False
        else:
            print("Sorry, please try again.\n")
            continue

    while encode == True:
        #If the user choose to encode, they will be prompted to enter a string, and then a encryption key.
        #Then the encrypted text will be returned to them.

        text_to_encode = string_input()

        key_encode = ask_for_key()

        stringed = encoder(text_to_encode,key_encode)
        print(' '.join(str(x) for x in stringed))
        break

    while encode != True:
        to_decode = number_input()

        key_decode = ask_for_key()

        print("Your decrypted text:")
        print(decoder(to_decode,key_decode))
        break

    replay = input("Do you want to continue? 'y' to continue, 'n' to quit. \n")
    if replay[0].lower() == 'y':
        choosing = True
        continue
    else:
        print("Goodbye.")
        break
    break
