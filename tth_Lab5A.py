
# Lab 5A - Numeric Converter
def main():
    while True:
        # Menu Prompt
        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit")

        ans = input("\nPlease enter an option: ")

        # Interpret response to call correct conversion
        if ans != "4":
            string = input("Please enter the numeric string to convert: ")

            match ans:
                case "1":
                    print("Result:", hex_string_decode(string), "\n")
                case "2":
                    print("Result:", binary_string_decode(string), "\n")
                case "3":
                    print("Result:", binary_to_hex(string), "\n")
                case "4":
                    print("Result:", hex_string_decode(string), "\n")
        else:
            exit()

def hex_char_decode(digit):
    # Match hex char w/ base 10 equivalent
    match digit:
        case "A":
            digit = 10
        case "a":
            digit = 10
        case "B":
            digit = 11
        case "b":
            digit = 11
        case "C":
            digit = 12
        case "c":
            digit = 12
        case "D":
            digit = 13
        case "d":
            digit = 13
        case "E":
            digit = 14
        case "e":
            digit = 14
        case "F":
            digit = 15
        case "f":
            digit = 15
    return digit

def hex_string_decode(hex):
    base10 = 0

    # Remove hex indicator
    if hex[1] == "x":
        hex = hex[2:]

    # Convert hex to base 10
    for i in range(0, len(hex)):
        num = int(hex_char_decode(hex[i]))
        position = len(hex) - i - 1
        position = 16**position
        num = num*position
        base10 += num
    return base10

def binary_string_decode(binary):
    base10 = 0

    # Remove binary indicator
    if binary[1] == "b":
        binary = binary[2:]

    # Convert binary to base 10
    for i in range(0, len(binary)):
        num = int(binary[i])
        position = len(binary) - i - 1
        position = 2**position
        num = num*position
        base10 += num
    return base10

def binary_to_hex(binary):
    # Declare 4-digit binary chunk and iteration vars
    quads = []
    hex = ""
    qCount = 0

    # Remove binary indicator
    if binary[1] == "b":
        binary = binary[2:]

    # Convert binary to hex
    for i in range(0, len(binary)):
        quads.append(binary[0])
        binary = binary[1:]
        qCount += 1

        if qCount == 4:
            qCount = 0
            num = binary_string_decode(quads)
            num = hex_char_encode(num)
            hex += str(num)
            quads = []
    return hex

def hex_char_encode(digit):
    # Match base 10 char with hex equivalent
    match digit:
        case 10:
            digit = "A"
        case 11:
            digit = "B"
        case 12:
            digit = "C"
        case 13:
            digit = "D"
        case 14:
            digit = "E"
        case 15:
            digit = "F"
    return digit
main()