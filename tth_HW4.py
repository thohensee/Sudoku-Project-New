from console_gfx import ConsoleGfx


def display_menu():
    print("\nRLE Menu\n"
          "--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data\n")
def to_hex_string(data):
    hString = ""

    for item in data:
        match item:
            case 10:
                item = "a"
            case 11:
                item = "b"
            case 12:
                item = "c"
            case 13:
                item = "d"
            case 14:
                item = "e"
            case 15:
                item = "f"
        hString = hString + str(item)

    return hString

def to_hex_string2(data):
    item = data

    match item:
        case '10':
            item = "a"
        case '11':
            item = "b"
        case '12':
            item = "c"
        case '13':
            item = "d"
        case '14':
            item = "e"
        case '15':
            item = "f"

    return item

def count_runs(data):
    if data == 0:
        return 0

    runCount = 1

    for i in range(1, len(data)):
        if data[i] != data[i - 1]:
            runCount = runCount + 1

    return runCount

def encode_rle(data):

    runs = []
    runs.append([data[0]])
    index = 0

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            if len(runs[index]) < 15:
                runs[index].append(data[i])
            else:
                runs.append([data[i]])
                index = index + 1
        else:
            runs.append([data[i]])
            index = index + 1

    rle = []

    for i in range(0, len(runs)):
        rle.append(len(runs[i]))
        rle.append(runs[i][0])

    return rle

def get_decoded_length(data):
    size = 0

    for i in range(0, len(data)):
        if i%2 == 0:
            size = size + data[i]

    return size

def decode_rle(data):
    string = []

    for i in range(0, len(data), 2):
        for j in range(0, data[i]):
            string.append(data[i + 1])

    return string

def string_to_data(string):
    data = []

    for i in range(0, len(string)):
        if string[i] >= "0" and string[i] <= "9":
            data.append(int(string[i]))
        else:
            match string[i]:
                case "a":
                    data.append(10)
                case "b":
                    data.append(11)
                case "c":
                    data.append(12)
                case "d":
                    data.append(13)
                case "e":
                    data.append(14)
                case "f":
                    data.append(15)

    return data

def to_rle_string(rle):
    string = ""

    for i in range(0, len(rle), 2):
        string = string + str(rle[i])
        toHex = [rle[i + 1]]
        string = string + to_hex_string(toHex)
        string = string + ":"

    string = string[:-1]

    return string

def string_to_rle(string):
    rle = []

    while True:
        if string.find(":") == -1:
            rle.append(string)
            break
        else:
            index = string.find(":")
            rle.append(string[:index])
            string = string[index + 1:]

    new_rle = []

    for i in range(0, len(rle)):
        if len(rle[i]) == 2:
            new_rle.append(int(rle[i][0]))
        else:
            new_rle.append(int(rle[i][:2]))

        last = string_to_data(rle[i][-1])
        num = int(last[0])
        new_rle.append(num)

    return new_rle

def hex_rle(rleString):
    hex = []
    toString = ''
    last = 0

    for i in range(len(rleString)):
        if rleString[i] == ':':
            hex.append(rleString[last: i])
            last = i

    length = len(rleString)
    hex.append(rleString[length - len(hex[len(hex) - 1]) + 1: length])

    for i in range(len(hex)):
        hex[i] = hex[i].replace(':', '')
        if len(hex[i]) > 2:
            hexChar = to_hex_string2(hex[i][0:2])
            hex[i] = hexChar + hex[i][-1]

    for item in hex:
        toString = toString + item

    return toString

def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print()
    image_data = None
    rleString = "(no data)"
    rleHex = "(no data)"
    flatHex = "(no data)"
    while True:
        display_menu()
        option = int(input("Select a Menu Option: "))

        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter the name of the file: ")
            image_data = ConsoleGfx.load_file(file_name)

            rleString = encode_rle(image_data)
            rleString = to_rle_string(rleString)

            rleHex = hex_rle(rleString)

            flatHex = to_hex_string(image_data)
        elif option == 2:
            image_data = ConsoleGfx.test_image
            print("Test image data is loaded")

            rleString = encode_rle(image_data)
            rleString = to_rle_string(rleString)

            rleHex = hex_rle(rleString)

            flatHex = to_hex_string(image_data)
        elif option == 3:
            rleString = input("Enter an RLE string to be decoded: ")
        elif option == 4:
            rleHex = input("Enter the hex string holding RLE data: ")
        elif option == 5:
            flatHex = input("Enter the hex string holding flat data:")
        elif option == 6:
            print("Displaying image...")

            if image_data == None:
                print("(no data)")
            else:
                ConsoleGfx.display_image(image_data)
        elif option == 7:
            print("RLE representation: " + rleString)
        elif option == 8:
            print("RLE hex values: " + rleHex)
        elif option == 9:
            print("Flat hex values: " + flatHex)
        else:
            print("Error! Invalid input.")

# Initialize
if __name__ == "__main__":
    main()