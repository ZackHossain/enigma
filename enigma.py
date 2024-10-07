
ASCII_OFFSET = 97

ROTOR_I = ['u','w','y','g','a','d','f','p','v','z','b','e','c','k','m','t','h','x','s','l','r','i','n','q','o','j']
ROTOR_II = ['a','j','p','c','z','w','r','l','f','b','d','k','o','t','y','u','q','g','e','n','h','x','m','i','v','s']
ROTOR_III = ['t','a','g','b','p','c','s','d','q','e','u','f','v','n','z','h','y','i','x','j','w','l','r','k','o','m']
REFLECTOR_B = ['y','r','u','h','q','s','l','d','p','x','n','g','o','k','m','i','e','b','f','z','c','w','v','j','a','t']

ROTOR_I = "ekmflgdqvzntowyhxuspaibrcj"
ROTOR_II = "ajdksiruxblhwtmcqgznpyfvoe"
ROTOR_III = "bdfhjlcprtxvznyeiwgakmusqo"

rotors = []
rotor1_pos = 0
rotor2_pos = 0
rotor3_pos = 0

#############
#   UTILS   #
#############

# converts ascii char to its index position in the alphabet
def toIndex(char):
    return ord(char) - ASCII_OFFSET

# converts a number from 0 to 25 into its ASCII character
# where 0 = a, 1 = b...
def toASCII(int):
    return chr(int + ASCII_OFFSET)

#############
#   CODE    #
#############


# Get the settings
print('Please Enter the Rotor Order: (format: 213)')
rotor_order = str(input())

a = int(rotor_order[0]) - 1
b = int(rotor_order[1]) - 2
c = int(rotor_order[2]) - 3

rotors_tmp = [ROTOR_I, ROTOR_II, ROTOR_III]
rotors = [rotors_tmp[a], rotors_tmp[b], rotors_tmp[c]]

print("Reflector: B (default)\n")

print('Please Enter the Rotor Positions: ')
rotor_pos = input().lower()

if (len(rotor_pos) != 3):
    print('Improper format: Please enter 3 letters.')
    exit(1)

rotor1_pos = toIndex(rotor_pos[0])
rotor2_pos = toIndex(rotor_pos[1])
rotor3_pos = toIndex(rotor_pos[2])

print("Enter the message to be encoded:")
message = input().lower()

# Encoding
encoded = ''
rotor1_start = rotor1_pos
rotor2_start = rotor2_pos
rotor3_start = rotor3_pos

for char in message:
    # skip non-letters
    if char < 'a' or char > 'z':
        encoded += char
        continue
    
    # set new rotor positions
    rotor1_pos = (rotor1_pos + 1) % 26
    if rotor1_pos == rotor1_start:
        rotor2_pos = (rotor2_pos + 1) % 26
        if rotor2_pos == rotor2_start:
            rotor3_pos = (rotor3_pos + 1) % 26
    
    # go through rotors
    index = (toIndex(char) + rotor1_pos) % 26
    char = rotors[0][index]
    
    index = (toIndex(char) + rotor2_pos) % 26
    char = rotors[1][index]
    
    index = (toIndex(char) + rotor3_pos) % 26
    char = rotors[2][index]
    
    # switchboard
    char = REFLECTOR_B[toIndex(char)]
    
    # go through rotors in reverse
    index = rotors[2].index(char)
    index = (index - rotor3_pos) % 26
    char = toASCII(index)

    index = rotors[1].index(char)
    index = (index - rotor2_pos) % 26
    char = toASCII(index)

    index = rotors[0].index(char)
    index = (index - rotor1_pos) % 26
    char = toASCII(index)
    
    encoded += char

print(encoded) 
    