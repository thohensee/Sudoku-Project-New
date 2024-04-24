
# Homework 3B - RLE with Images

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

def count_runs(data):
    if data == 0:
        return 0

    runCount = 1

    for i in range(1, len(data)):
        if data[i] != data[i - 1]:
            runCount = runCount + 1

    return runCount

def encode_rle(data):
    if data == None:
        return None

    runs = []
    runs.append([data[0]])
    index = 0

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            runs[index].append(data[i])
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
