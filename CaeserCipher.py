# Simple encoding algorithm that uses ROT# (You can change it to be whatever you want...)

def shift(text, shift):
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

print(shift("hello", 13))


        
