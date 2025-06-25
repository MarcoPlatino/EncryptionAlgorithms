# Simple encoding algorithm that uses ROT# (You can change it to be whatever you want...)

def encode(text, shift):
    listShift = list(text)
    encodedList = []
    for i in listShift:
        base = ord(i)
        over = base + shift
        if over > 122:
            dif = 122 - (base + shift)
            print(dif)
            encodedList.append(chr(96 + abs(dif)))
            continue
        encodedList.append(chr((base) + (shift)))
    return "".join(encodedList)

# print(encode("hello", 13))

def unencode(text, shift):
    listShift = list(text)
    encodedList = []
    for i in listShift:
        base = ord(i)
        under = base - shift
        if under < 97:
            dif = 98 - (base + shift)
            encodedList.append(chr(123 - abs(dif)))
            # print(chr(122 - abs(dif)))
            continue
        encodedList.append(chr((base) - (shift)))
    return "".join(encodedList)

        
